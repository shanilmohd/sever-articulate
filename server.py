from flask import Flask
import requests

app = Flask(__name__)

@app.route("/req/<prompt>")
def req(prompt):
    a = requests.get("https://090c-34-83-11-209.ngrok-free.app/?prompt="+prompt)
    return(a.text)
if __name__=="__main__":
    app.run()
