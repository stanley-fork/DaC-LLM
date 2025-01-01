import json

def main():
    problems_answers = []

    while True:
        problem = input("Enter a problem (or type 'exit' to finish): ")
        if problem.lower() == 'exit':
            break
        answer = input("Enter the answer for the problem: ")

        problems_answers.append({
            "problem": problem,
            "answer": answer
        })

    # Ask the user for the file name
    file_name = input("Enter the file name to save the JSON (with .json extension): ")

    # Write to the specified file
    with open(file_name, 'w') as json_file:
        json.dump(problems_answers, json_file, indent=2)

    print(f"Data saved to {file_name}")

if __name__ == "__main__":
    main()
