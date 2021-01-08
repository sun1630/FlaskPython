
from flask import jsonify
from FlaskWebProject import app

@app.route("/api/getStr1", methods = ['GET'])
def GetStr1():
    return jsonify({'v':"hello world11"})
