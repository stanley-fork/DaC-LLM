# Dac-LLM
This repository showcases our recent research aimed at improving the accuracy of large language models (LLMs) in mathematical domains. We believe our approach has surpassed previous methods, such as chain-of-thought and graph-of-thought techniques, achieving state-of-the-art performance.

## Background
In recent years, numerous prompting methods have been developed to guide large language models (LLMs) in tackling mathematical problems. However, their mathematical performance still falls short of satisfaction espically without fine tuning or zero-shot prompting. As a result, we have devised a novel approach to enhance this performance, which we call "divide and conquer." Unlike traditional applications of divide and conquer, our method proposes utilizing a programming language, such as Python, combined with an interpreter, simulating the way a human uses a calculator.

## Algorithm (2024-12-31 Update)

### Dac Algorithm
<img width="703" alt="Screenshot 2025-01-01 at 1 49 49 PM" src="https://github.com/user-attachments/assets/33a0d20d-f92f-4be3-9a1b-3ced0477e0fd" />
<br/>

### Perofrmance Analysis
![Screenshot 2025-01-01 at 3 26 21 PM](https://github.com/user-attachments/assets/dcd32ed2-6d9b-44a1-8c04-c6f9379c9bc1)



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

## Paper
Our paper is currently in progress. If you are interested in collaborating with us, please feel free to reach out! Any feedback are hugely appreciated.

## Author
Hon Kit Long u3608018 [at] connect.hku.hk 
<br>
Au Chi Kin Kinson chikinau03 [at] gmail.com
<br>
Liu Peter Hong Zhiliuhongzhi3000 [at] gmail.com
<br>
Cho Chung Hei u3605966 [at] connect.hku.hk


## License
This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
