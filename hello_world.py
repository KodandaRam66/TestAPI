from flask import Flask, request, jsonify, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/hello-world", methods=['GET'])
def get_hello_world():
    return jsonify({"message":"Hello"})

@app.route("/test", methods=['POST', 'GET'])
def greetings():
    if request.method == "POST":
        user = request.form["name"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("test.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>Hello {usr}!!</h1>"


if __name__ == "__main__":
    app.run(debug=True)