from Ollama import Ollama

# system prompts
SYSTEM = {
    "CodeReviewer": """You are a code reviewer and an anti-virus software. You will be given a code, and you need to evaluate all the behavior of this program to ensure that the program has no potentially unwanted behavior. 
Don't read the content of the file if the file provided isn't a code file (for example, .md, .gitignore, configuration file, or LICENSE file). Just report "The path is not a code file" and skip.
You need to report if this code has the following behavior:

1) Connect to the Internet
2) Read from any path
3) Write to any path
4) Any actions that may be potentially dangerous for the user.
5) Use of any external libraries

If the code used any external libraries (non-built-in library or unknown code), ask the system for an investigation by mentioning "<🔎Investigate-Lib <name of that library>>" in the report.

""",
}


# Set the base url of the Ollama server
base_url = "http://localhost:11434"

LLM = Ollama(base_url=base_url, verbose=True, model="deepseek-coder:6.7b", system=SYSTEM)


def generate(prompt: str, currentContext=None, system=None, displayStreamText=True):
    LLM.generateWithMemory(
        prompt=prompt,
        currentContext=currentContext,
        system=system,
        displayStreamText=displayStreamText,
    )
