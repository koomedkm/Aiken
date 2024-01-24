#!/usr/bin/python3
def text_to_aiken(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        text = input_file.read()

    lines = text.split('\n')
    questions = []
    current_question = None

    for line in lines:
        line = line.strip()

        if line.startswith('Q:'):
            if current_question:
                questions.append(current_question)
            current_question = {'question': line[2:], 'choices': []}
        elif line.startswith('A:'):
            if current_question:
                current_question['choices'].append(line[2:])

    if current_question:
        questions.append(current_question)

    aiken_format = ""
    for idx, question in enumerate(questions):
        aiken_format += f"{idx + 1}. {question['question']}\n"
        for i, choice in enumerate(question['choices']):
            aiken_format += f"   {'ABCDE'[i]}. {choice}\n"

    with open(output_file_path, 'w') as output_file:
        output_file.write(aiken_format)

# Example usage:
input_file_path = 'input.txt'
output_file_path = 'output.txt'

text_to_aiken(input_file_path, output_file_path)

