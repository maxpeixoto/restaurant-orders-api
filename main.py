from flask import Flask
app = Flask(__name__)
application=app


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/restaurant')
def restaurant():
  return "many restaurants"

if __name__ == '__main__':
    app.run()
