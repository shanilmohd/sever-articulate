from flask import Flask
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/req/<prompt>")
@cross_origin()
def req(prompt):
    a = requests.get("https://53f8-34-123-227-10.ngrok-free.app/?prompt="+prompt)
    return(a.text)
if __name__=="__main__":
    app.run()
