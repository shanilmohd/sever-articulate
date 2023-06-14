from flask import Flask
import requests

app = Flask(__name__)

@app.route("/req/<prompt>")
def req(prompt):
    a = requests.get("https://e56c-34-142-142-176.ngrok-free.app/?prompt="+prompt)
    return(a)
if __name__=="__main__":
    app.run()
