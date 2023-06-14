from flask import Flask
import requests

app = Flask(__name__)

@app.route("/req/<prompt>")
def req(prompt):
    a = requests.get(" https://4afa-34-142-142-176.ngrok-free.app/?prompt="+prompt)
    return(a.text)
if __name__=="__main__":
    app.run()
