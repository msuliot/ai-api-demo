# AI API Demo

This demo has 2 github dependencies

React UI - (ai-react-demo)
https://github.com/msuliot/ai-react-demo

API - (ai-api-demo)
https://github.com/msuliot/ai-api-demo

## Installation

1. Must have Python3.
2. Get repository clone or download
```bash
git clone https://github.com/msuliot/ai-api-demo.git 
```
3. use pip or pip3 to install any dependencies.
```bash
pip install openai
pip install llama-index
pip install Flask
pip install Flask-Cors
```

## Usage

Make sure to get an OpenAI key from https://platform.openai.com/account/api-keys

Create a ".env" file and put your OpenAI key in that file
```bash
OPENAI_API_KEY='your key here'
```

Then, delete the placeholder-delete-this files in the data and storage directories.

Then, save any PDFs in the 'data' directory.

Then run your data importer in VS Code or
```bash
python3 data_import.py
```
When the process is complete it will store result in a vector database located in the 'storage' directory

## To run the API in dev mode, use the following command:

```bash
python3 app.py
```

## Notes

This demo app will be called by the React UI
(ai-react-demo) https://github.com/msuliot/ai-react-demo
