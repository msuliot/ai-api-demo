import os
import _util
import _rules

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data = {'prompt': "",'response': "",}

@app.route('/api', methods=['POST'])
def get_variable():
    prompt = request.form.get('prompt')
    data['prompt'] = _util.decode(prompt)
    return _rules.get(data)

##### LOCAL #######
if __name__ == '__main__':
    print('Running API')
    app.run(host="0.0.0.0", port=8000)