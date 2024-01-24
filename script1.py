def text_to_aiken(text):
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

    return aiken_format

# Example usage:
input_text = """
Q: What is the capital of France?
A: London
B: Madrid
C: Berlin
D: Paris
"""

result = text_to_aiken(input_text)
print(result)

