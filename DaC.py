import pandas as pd
import json
import os
from openai import OpenAI
import io
import sys
import contextlib

def execute_python_code(code):
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        try:
            exec(code)
            return output.getvalue().strip()
        except Exception as e:
            return f"Error: {str(e)}"

def solve_with_python(problem, client, model, max_iterations=5):
    messages = []
    iteration = 0
    
    system_prompt = """You are an expert mathematical problem solver. Follow these steps:
1. First analyze if the problem can be solved with Python code.
2. If yes, provide clear, executable Python code with necessary imports.
3. If not, break down into smaller sub-problems.
4. For answers, provide:
   - Both symbolic expression AND numerical value when possible
   - Start with 'CONFIDENT:' if you're sure of the answer
   - Use LaTeX for mathematical expressions (e.g., $\frac{3}{4}$)
5. Keep track of intermediate results and build upon them.
6. Verify your solutions when possible."""

    messages.append({
        "role": "system",
        "content": system_prompt
    })
    messages.append({
        "role": "user",
        "content": f"Problem: {problem}\nAnalyze and solve this problem. If possible, provide Python code. Otherwise, break it down into steps."
    })
    
    solution_attempts = []
    subquestions = []
    
    while iteration < max_iterations:
        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7,
            max_tokens=1000
        )
        
        response = completion.choices[0].message.content
        solution_attempts.append(response)
        messages.append({"role": "assistant", "content": response})
        
        if response.startswith("CONFIDENT:"):
            return {
                "final_answer": response.replace("CONFIDENT:", "").strip(),
                "iterations": iteration + 1,
                "solution_attempts": solution_attempts,
                "subquestions": subquestions
            }
        
        if "Step" in response or "Problem" in response:
            for line in response.split('\n'):
                if (line.startswith(('Step', 'Problem', '•', '-', '*')) or 
                    any(str(i) + '.' in line for i in range(1, 10))):
                    subquestions.append(line.strip())
        
        if "```python" in response:
            code_blocks = response.split("```python")
            for block in code_blocks[1:]:
                code = block.split("```")[0].strip()
                execution_result = execute_python_code(code)
                
                messages.append({
                    "role": "user",
                    "content": f"The Python code execution resulted in: {execution_result}\n"
                             "Based on this result, please provide:\n"
                             "1. The mathematical expression (using LaTeX if needed)\n"
                             "2. The numerical value\n"
                             "Start with 'CONFIDENT:' if you're sure of both."
                })
        else:
            messages.append({
                "role": "user",
                "content": "Can any part be solved with Python now? If yes, provide the code. "
                          "If not, continue breaking down the problem. "
                          "Remember to provide both expression and numerical forms when possible."
            })
        
        iteration += 1
        
        if iteration >= max_iterations:
            messages.append({
                "role": "system",
                "content": "Provide your final answer now, including both expression and numerical value if possible. "
                          "Start with 'CONFIDENT:' if you're sure."
            })
            final_completion = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.7,
                max_tokens=100
            )
            return {
                "final_answer": final_completion.choices[0].message.content.replace("CONFIDENT:", "").strip(),
                "iterations": iteration,
                "solution_attempts": solution_attempts,
                "subquestions": subquestions
            }
    
    return None

def read_config(config_file='config.json'):
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

def main():
    config = read_config()
    
    # Load the dataset
    df = pd.read_json(config['input_file'], lines=False)
    
    client = OpenAI(base_url=config['base_url'], api_key=config['api_key'])
   
    results = []
    
    # Load existing results if the file exists
    if os.path.exists(config['output_file']):
        with open(config['output_file'], 'r') as f:
            results = json.load(f)
    
    start_index = len(results)
    
    try:
        for i in range(start_index, len(df)):
            print(f"Processing question {i + 1} of {len(df)}")
            problem = df['problem'].iloc[i]
            ground_truth = df['answer'].iloc[i]
            
            solution = solve_with_python(problem, client, config['model'])
            
            entry = {
                'problem_index': i,
                'problem': problem,
                'ground_truth': ground_truth,
                'solution': solution['final_answer'],
                'iterations_needed': solution['iterations'],
                'solution_attempts': solution['solution_attempts'],
                'subquestions': solution['subquestions']
            }
            
            results.append(entry)
            
            # Save after each iteration
            with open(config['output_file'], 'w') as f:
                json.dump(results, f, indent=2)
            
            print(f"Completed question {i + 1} in {solution['iterations']} iterations")
            print(f"Generated {len(solution['subquestions'])} subquestions")
            print("-" * 50)
            
    except Exception as e:
        print(f"Error occurred at index {i}: {str(e)}")
        with open(config['output_file'], 'w') as f:
            json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()
