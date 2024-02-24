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
    try:
        with open(file_path, 'r') as file:
            code_content = file.read()
    except:
        print("Error reading file")
        return

    # Set the system prompt
    system_prompt = config.SYSTEM["CodeReviewer"]

    prompt = "File Path: " + file_path + "\n\nCode Content:\n\n" + code_content

    # Call Ollama
    return config.generate(prompt=prompt, system=system_prompt)




def summarizeReports(reports):
    print("\n\n\n ========= Summary of Reports ========= \n\n")
    system_prompt = config.SYSTEM["ReportSummarizer"]
    print(config.generate(prompt=reports, system=system_prompt))
    print("\n\n\n")


# Example usage
def __init__():
    file_path = input("Enter the path of the code file: ")
    evaluateCodeFile(file_path)