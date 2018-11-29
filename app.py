from flask import Flask, request
#from flask_restful import Resource, Api

app = Flask(__name__)
#api = Api(app)

company_factors = {}

@app.route('/', methods=['GET', 'POST'])
def main():
    import json
    return ''' hell word '''

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