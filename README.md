# AI API Demo

## This demo has 2 github dependencies that must be installed in order to run the full demo:

React UI - (ai-react-demo) 
https://github.com/msuliot/ai-react-demo

API - (ai-api-demo)
https://github.com/msuliot/ai-api-demo

## Installation for API

1. Must have Python3.
2. Get repository clone or download
```bash
git clone https://github.com/msuliot/ai-api-demo.git 
```
3. use pip3 to install any dependencies.
```bash
pip3 install --upgrade -r requirements.txt
```

## Usage

Make sure to get an OpenAI key from https://platform.openai.com/account/api-keys

Create a ".env" file and put your OpenAI key in that file
```bash
OPENAI_API_KEY='your key here'
```

## Create your OpenAI fine-tuning model
- Full automatic will run the entire process from start to finish.
- full_automatic.py and sample data.jsonl file is located in the create_model folder. 
- Data must be in json lines format.
    ```bash
    python3 full_automatic.py
    ```
- You will the model_id from the output of the full automatic process.
- This process can take OpenAI about 5-20 minutes to complete.

- Update the _api.py file with your model_id
    
## To run the API in dev mode, use the following command:

```bash
python3 app.py
```

The API will run on port 8000 by default.

## Notes

This demo app will be called by the React UI
(ai-react-demo) https://github.com/msuliot/ai-react-demo
