from flask import Flask

app = Flask(__name__)

@app.route("/hellosocar", methods=['GET'])
def hello():
  return "hello socar"

@app.route("/", methods=['GET'])
def hello123():
  return "hello koo"
