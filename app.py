from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

  
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

with app.app_context():
    db.create_all()
  

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        msg = request.form["message"]
        new_msg = Message(name=name, message=msg)
        db.session.add(new_msg)
        db.session.commit()
        return render_template("thankyou.html", user_name=name)
    return render_template("index.html")

@app.route("/messages")
def messages():
    all_messages = Message.query.all()
    return render_template("thankyou.html", messages=all_messages)
if __name__ == "__main__":
    app.run(debug=True)
