from flask import Flask 
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

"""실행법
export FLASK_APP=파일이름.py
flask run
-터미널에 입력 """
""" 종료 
ctrl + c"""