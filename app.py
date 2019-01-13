from flask import Flask, request, jsonify
#from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from neural_net import NeuralNet

app = Flask(__name__)

net = NeuralNet()
net.init_model()

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def main():
    body = request.get_json()
    company = [(body['askedFor']), (body['exchangeForStake']), (body['valuation']), body['industry']]
    net.init_model()
    ans = net.predictOffer(company)
    print(ans, 'for comp', (company))
    return jsonify(ans)

if __name__ == '__main__':
    app.run(debug=True)