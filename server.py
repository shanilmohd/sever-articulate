from flask import Flask
import requests

app = Flask(__name__)

@app.route("/req/<prompt>")
def req(prompt):
    a = requests.get("https://53f8-34-123-227-10.ngrok-free.app/?prompt="+prompt)
    return(a.text)
if __name__=="__main__":
    app.run()
