from flask import jsonify
from llama_index import StorageContext, load_index_from_storage

import openai

# get keys from .env file
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def get(data):
    print(data)
    try:
        storageDB = './storage'
        storage_context = StorageContext.from_defaults(persist_dir=storageDB)
        index = load_index_from_storage(storage_context)
        query_engine = index.as_query_engine()
        response = query_engine.query(data['prompt'])
        data['response'] = response.response
    except Exception as ex:
        data['response'] = str(ex)

    return jsonify(data)

    