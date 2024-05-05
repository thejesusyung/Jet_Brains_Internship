import os
import re
import pandas as pd


def process_kotlin_files(directory):
    dataset = []

    for root, dirs, files in os.walk(directory):  # Use os.walk to traverse directories
        for filename in files:
            if filename.endswith('.kt'):
                file_path = os.path.join(root, filename)
                print("Processing Kotlin file:", file_path)

                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                for i in range(1, len(lines)):
                    start_index = max(0, i - 65)
                    context = "".join(lines[start_index:i]).strip()
                    completion = lines[i].strip()
                    dataset.append({'Context': context, 'Completion': completion})

    if dataset:
        print("Dataset contains", len(dataset), "entries")
    else:
        print("Dataset is empty")

    df = pd.DataFrame(dataset)
    df.to_csv('kotlin_dataset.csv', index=False)


# Ensure the directory path is correct


# Specify the directory containing Kotlin files
directory_path = '/Users/maxim/Desktop/Codes/Kotlin/kotlin/'
process_kotlin_files(directory_path)


# Usage example
#df_functions = find_kotlin_functions('/Users/maxim/Desktop/Codes/Kotlin/kotlin')
#df_functions.to_csv('ALL_FUNCTIONS_FROM_KOTLIN.csv', index=False)
#print(len(df_functions))