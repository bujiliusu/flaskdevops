from flask import Flask,jsonify,abort,make_response
from flask import request

app = Flask(__name__)

tasks = [
    {
        "id":1,
        "title":u'buy',
        "description":u'Chinese',
        "done":False
    },
    {
        "id":2,
        "title":u'sell',
        "description":u'France',
        "done":False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_tasks(task_id=None):
    if task_id:
        task = [ i for i in tasks if i['id']==task_id]
        print(task)
        if len(task) == 0:
            abort(404)
        return jsonify({'task':task})
    else:
        return jsonify({'tasks':tasks})
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'not found'}),404)

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    print(type(request.json))
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('desc',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({'tasks':task}),201
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
