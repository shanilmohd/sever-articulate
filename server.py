from flask import Flask
import requests

app = Flask(__name__)

@app.route("/req/<prompt>")
def req(prompt):
    a = requests.get("https://a7db-35-204-126-85.ngrok-free.app/?prompt="+prompt)
    return(a.text)
if __name__=="__main__":
    app.run(debug=True)