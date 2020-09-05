from flask import jsonify,Flask,request,render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app, supports_credentials=True)
@app.route('/api/getdata')
def index():
    tokendata = request.headers.get('token')
    print(tokendata)
    data = {'name':'test'}
    return jsonify(data)
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')