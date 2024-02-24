import os
import config




def evaluateCodeFile(file_path):
    if(os.path.exists(file_path) == False):
        print("File does not exist")
        return
    if(os.path.isfile(file_path) == False):
        print("The path is not a file")
        return
    
    print("\n\n\n ========= Code Security Report ========= ")
    print("Code file evaluated: " + file_path, end="\n\n")
    
    # Read the content of the code file
    with open(file_path, 'r') as file:
        code_content = file.read()

    # Set the system prompt
    system_prompt = config.SYSTEM["CodeReviewer"]

    prompt = "File Path: " + file_path + "\n\nCode Content:\n\n" + code_content

    # Call Ollama using litellm
    config.generate(prompt=prompt, system=system_prompt)

def FakeevaluateCodeFile(file_path):
    print("Evaluating code file: " + file_path)


def writeToFile(dir_path, file_name, content):
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, "a") as file:
        file.write(content)


# Example usage
def __init__():
    file_path = input("Enter the path of the code file: ")
    evaluateCodeFile(file_path)