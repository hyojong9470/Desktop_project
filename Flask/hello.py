from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/h1')
def hey_gyus():
    return "hey guys"

if __name__=="__main__":
    app.run()