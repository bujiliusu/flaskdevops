from flask import Flask
from flask_sqlalchemy  import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1/devops'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
# db.create_all()
# admin = User('admin', 'admin@example.com')
# db.session.add(admin)
# db.session.commit()
print(User.query.all())
print(User.query.filter_by(id=1).first())