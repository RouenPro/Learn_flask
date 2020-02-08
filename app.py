from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to Flask framework'

app.run(port=5000)