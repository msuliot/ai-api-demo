# AI API Demo

This application is designed to generate a refined OpenAI model by fine-tuning it to perform optimally. The demonstration includes a user interface built with React to emulate a chatbot powered by a custom, fine-tuned model. This model can be accessed via a Python API, which facilitates seamless interaction between the frontend and the backend. This ensures not only an interactive and responsive user experience but also enables the application to harness the full potential of the custom-trained model.

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
- You will need the model_id from the output of the full automatic process.
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
