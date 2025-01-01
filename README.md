# Dac-LLM
This repository showcases our recent research aimed at improving the accuracy of large language models (LLMs) in mathematical domains. We believe our approach has surpassed previous methods, such as chain-of-thought and graph-of-thought techniques, achieving state-of-the-art performance.

## Background
In recent years, numerous prompting methods have been developed to guide large language models (LLMs) in tackling mathematical problems. However, their mathematical performance still falls short of satisfaction. As a result, we have devised a novel approach to enhance this performance, which we call "divide and conquer." Unlike traditional applications of divide and conquer, our method proposes utilizing a programming language, such as Python, combined with an interpreter, simulating the way a human uses a calculator.

## Algorithm

### Dac Algorithm
<img width="703" alt="Screenshot 2025-01-01 at 1 49 49 PM" src="https://github.com/user-attachments/assets/33a0d20d-f92f-4be3-9a1b-3ced0477e0fd" />
<br/>

### Explain
Our algorithm primarily focuses on mathematical problems, particularly computational challenges rather than proof-based issues. It first assesses whether the problem is a mathematical one and then divides it into subproblems until it can be solved using Python programming. This approach significantly reduces calculation errors, and we believe that our performance, even without fine-tuning the model, has reached state-of-the-art levels.

## Performance 
Currently, our experiments with other models and datasets are still in progress. However, here are some experimental results using the DeepSeek v3 model. Some result materials are provided. 

| Method                             | Score      |
|------------------------------------|------------|
| Direct Prompting                   | 271 / 500  |
| Our Method (Multiple Attempts)     | 441 / 500  |
| Our Method (One Attempt)           | 407 / 500  |

## Usage
Your dataset should be in a JSON file containing problems and their corresponding answers. Additionally, Python installation is necessary.

## License
This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

## Paper
Our paper is currently in progress. If you are interested in collaborating with us, please feel free to reach out!

## Author
Hon Kit Long u3608018 [at] connect.hku.hk
Kinson Au
Liu Peter Hong Zhiliuhongzhi3000 [at] gmail.com
Cho Chung Hei u3605966 [at] connect.hku.hk

