# DocsGPT
Chat with your documents using embeddings and gpt-3.5-turbo by OpenAI

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Ideas](#ideas)
- [Contributing](#contributing)
- [License](#license)

## [Introduction](introduction)
This project allows you to chat with your documents, books, scripts, etc., as long as they are in the .pdf format. 
To acquire this capability, the project uses embeddings (generated with the OpenAI API) and feeds them back through a ConversationalRetrieverChain provided by Langchain. 
This way, you are able to pass the embeddings with your prompt to OpenAI and send specific prompts about your document, 
such as 'Write a summary about chapter XY' or 'Generate a short summary of chapter XY in bullet points for a PowerPoint presentation'.

## [Installation](installation)

- Clone the Project, and install the requirements using the following snippet
```shell
$ git clone git@github.com:jimmymeister98/DocsGPT.git
$ cd DocsGPT
$ pip install -r requirements.txt
```
- (Eventually install additional requirements thrown in the console on runtime, which i didnt track yet)
- Get your OpenAI API key and paste it into the .env file (Embedding and Prompting costs are listed [on the OpenAI Pricing page](https://openai.com/pricing) the models used are "text-embedding-ada-002-v2" and "gpt-3.5-turbo")
- Paste the path of your file in the variable `pdf_path` in `main.py` (subject to change, will probably change to a prompt in near future)
- run with `python main.py` or by clicking the run button in the IDE of your choice

## [Usage](usage)

```shell
$ python main.py
```

## [Features](features)

- Persistent Vector Stores: Vector stores are stored locally, so embeddings only need to be generated once per document.
  - Deep Lake: You can either store your Vector Stores locally or visualize and host them on [ActiveLoop](https://app.activeloop.ai/) with minimal changes. The ability to switch between local and remote storage will be added later.
- Prompt Chaining: With the use of history-aware prompting, it is possible to chain prompts together. For example: "...add a short summarizing sentence to the previous prompt" 

## [Ideas](ideas)

- Local Embedding: Create embeddings locally using LLAMA and a fitting model (7b for the beginning)
- Local Prompting: Prompt against a local LLM like GPT4ALL, Vicuna or LLAMA
  - (Both will need rather beefy hardware, but will cut the cost of embedding and prompting)
 - Add prompting for files and increase prompting in general
 - Add a gpt-like web ui
 - Switch between local and remote saving of embeddings

## [Contributing](contributing)

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Submit a pull request.

## [License](license)

This project is licensed under the [To be licensed](LICENSE).
