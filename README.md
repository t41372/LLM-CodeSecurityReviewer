# LLM-CodeSecurityReviewer
[Proof of concept stage]

Use LLM to check source code (codebase) for potentially unwanted behaviors.









## Installation

python 11

~~~sh
pip install requests
~~~



This project uses Ollama as the LLM backend. You need a running Ollama server to use this project. Should you wish to use a remote Ollama server, you will need to change the base url setting in the config.py file.

## Run

Scan the whole directory

~~~ sh
python traverse.py
~~~

Use `reviewFile.py` instead if you only want to scan a single file.

~~~ sh
python reviewFile.py
~~~ 



