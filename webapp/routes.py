from config import app

@app.route("/")
def greet():
    return "Flask App is running..!!!"