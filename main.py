from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    print(f"request的attribute method:{request.method}")
    print(f"request的attribute method:{request.mimetype_params}")
    return render_template('index.html')