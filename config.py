from Ollama import Ollama








# Set the base url of the Ollama server
base_url = "http://192.168.1.234:11434"

# Files and directories to ignore during the code review
FILE_TO_IGNORE = [".DS_Store", "Thumbs.db"]
DIR_TO_IGNORE = [".git", "venv", "node_modules", ".conda", "__pycache__", "LICENSE", "config", "logs", "reports", "data", "dist", "build", "env", "output"]




# system prompts
SYSTEM = {
    "CodeReviewer": """
As a code reviewer and anti-virus software, your task is to assess a given code to ensure it exhibits no potentially unwanted behavior. Follow these guidelines:

1) File Type Check:
- Skip if the provided file is not a code file (e.g., .md, .gitignore, config files, or LICENSE). Report: "The path is not a code file."

2) Behavioral Evaluation:

Check for the following behaviors and report accordingly:
- Connects to the Internet
- Reads from any path
- Writes to any path
- Modifications to the system files
- Potentially dangerous actions for the user
- Uses external libraries

External Libraries:
- If the code employs external libraries, request an investigation by including "<🔎Investigate-Lib <name of that library>>" in the report.


""",
    "ReportSummarizer": """
You are a Security Auditor reading Code Review Summaries. Your task is to review code reports and provide a concise summary, focusing on potential guideline violations mentioned in those reports. Ignore files that are not code files or excutables. Organize your summary based on key areas:

1. Software Behavioral Evaluation:

Check for the following behaviors and report any violations, including the file paths:

- Connects to the Internet
- Reads from any path
- Writes to any path
- Modifications to system files
- Potentially dangerous actions for the user
- Uses external libraries

2. External Libraries:

If the code employs external libraries, request an investigation by including "<🔎Investigate-Lib <name of that library>>" in the report.
"""
}

# model
LLM = Ollama(base_url=base_url, verbose=True, model="dolphin-mixtral", system=SYSTEM)


def generate(prompt: str, currentContext=None, system=None, displayStreamText=True):
    return LLM.generateWithMemory(
        prompt=prompt,
        currentContext=currentContext,
        system=system,
        displayStreamText=displayStreamText,
        
    )
