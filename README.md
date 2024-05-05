# JB_LLM

## Introduction

Please note that although this internship task was open for longer, due to my focus on participating in JASS 2024 (hosted by JetBrains) and subsequently focusing on my first exams in English, I had about a week to concentrate on 4 internship tasks. **Please do not perceive this comment as a complaint or self-pity because it is not.** Instead, I am highlighting that a lot of hard work was invested. Especially considering my major is Math & Stats, not CS, so I tend to code slower than many.

## Project Overview

Although I would not call it a success, I would like to guide you through what was accomplished:

After some initial research on the topic of code-completion ([Paper 1](https://arxiv.org/abs/2401.06391), [Paper 2](https://arxiv.org/abs/2401.01701), [Article 3](https://core.ac.uk/display/590709716?source=2), and most importantly this [JetBrains News Article](https://blog.jetbrains.com/blog/2024/04/04/full-line-code-completion-in-jetbrains-ides-all-you-need-to-know)), I decided to focus on one-line completion. Initially, I experimented with completing only methods and functions in Python because the Phi1.5 paper hints that the model is good at completing a description of a function. To my surprise, the result was decent. A simple trick I used was to limit the token size to a smaller size for time optimization purposes, then I post-processed the output and simply discarded everything after the '\n' symbol. Unfortunately, Phi1.5 either does not have a properly functioning option to add a stop_token, or I was not able to add it correctly.

Later, I started gathering Kotlin code. I downloaded the language itself from GitHub and the script I ironically named 'gather_python_dataset.py' actually collects Kotlin code, not Python. There, if you specify a directory where to look for Kotlin code and another one (or the same) to save the resulting dataset, it parses the Kotlin well. Then, in a `Random_sample_creation_eda.ipynb`, I experimented with what kind of rows to throw away and created random subsamples to work with (note that the subsamples range from 500 to 5000 in length and the total Kotlin dataset is 3m rows before EDA and 2m after, so even though our method of parsing data creates too many instances of code completion rows from large files, it does not affect the variability of samples that much due to a large discrepancy of the sizes of the whole code and subsamples).

## Challenges and Learning

The best but the hardest part was fine-tuning, and here you can run the notebook Phi1.5 to do fine-tuning, and model weights will be saved in a local directory and later in the notebook, they can be used to do predictions. Unfortunately, my largest mistake (except doing 4 internship tasks in parallel instead of one by one) was not being familiar enough with Colab and believing that at a Pro subscription, files are saved after running. That is not true, and I lost my tuned model right in the process of downloading it to my laptop. After that, I did not have enough compute to do it again.

However, testing and playing around with the fine-tuned model myself made me believe that it indeed got better. Ironically, if you do not truncate the answer to one line, more noticeable improvements I personally found in predicting a few lines at the same time.

## Conclusion

The model does work, I learned a lot and got better and smarter. I want to say thank you for an interesting internship task. It was a lot of fun spending a few dozen hours on this. I will continue to grow my LLM skills, and if that is possible to do under the watch of JetBrains, I would have been immensely appreciative. Take care!
