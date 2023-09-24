from flask import Flask, request
from mock_data import *
from flask_cors import CORS

#set envrionment variables
#export FLASK_APP = application.py
#export FLASK_ENV=development

#instantiate flask application
app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "localhost:4200"}})
CORS(app)

#create endpoints
# #create homepage route <yoururl>
@app.route('/')
@app.route('/home')
def home_page():
    return 'Welcome, You are on HomePage!'

@app.route('/api/dummy')
def dummy_data():
    return mockData

#create query endpoint <yoururl>/query
@app.route('/api/query')
def query_page():
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')
    result = param1 + param2
    return 'The sum of params {}, and {} is {}'.format(param1, param2, result)

#create sum endpoint <yoururl>/sum
@app.route('/api/calculate', methods=['POST'])
def sum_page():
    data = request.get_json()
    x = data['x']
    y = data['y']
    sum = int(x) + int(y)
    diff = abs(int(x) - int(y))
    return {"sum": sum, "diff": diff}

@app.route('/about')
def about_page():
    return 'About Page'

if __name__ == '__main__':
    app.run(debug=True, port=8080)


