# ------ > Run the command below in the terminal, use -- printenv -- to validate OPENAI_API_KEY
# export OPENAI_API_KEY="your_key_from_openai"
# OR
# import os
# os.environ["OPENAI_API_KEY"] = 'YOUR_OPEN_AI_KEY'

from flask import jsonify
import openai
from llama_index import StorageContext, load_index_from_storage

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

    