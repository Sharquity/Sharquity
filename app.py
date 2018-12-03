from flask import Flask, request, jsonify
#from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from neural_net import NeuralNet


net = NeuralNet()
net.init_model()

app = Flask(__name__)
#api = Api(app)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

company_factors = {}

@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def main():
    import json
    body = request.get_json()
    print(body)
    return jsonify(net.predictOffer((body['askedFor'], body['exchangeForStake'], body['valuation'], body['industry'])))

@app.route('/eval', methods=['POST'])
def evalution():
    offer = request.form['offer']
    percent = request.form['percent']
    return ''' '''

'''
class CompanyPredictions(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(CompanyPredictions, '/<string:todo_id>')
'''

if __name__ == '__main__':
    app.run(debug=True)