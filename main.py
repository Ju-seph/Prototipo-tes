from flask import Flask, request
import controllers.index as indx
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, static_folder='static', static_url_path="")
app.secret_key= os.getenv("KEY")

@app.after_request
def after_request(response):
    response.headers["cache-control"]= "no-cache, no-store, must-revalidate"
    return response

@app.route('/',methods=["GET", "POST"])
def index():
    return indx.inicio(request)


if __name__ == "__main__":
    app.run(host=os.getenv("HOST"), port=os.getenv("PORT"))