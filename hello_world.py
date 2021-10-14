from flask import Flask, request, jsonify, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/hello-world", methods=['GET'])
def get_hello_world():
    return jsonify({"message":"Hello"})

@app.route("/test", methods=['POST', 'GET'])
def greetings():
    if request.method == "POST":
        user = request.form["name"]
        target = request.form["targets"]
        print(user)
        if user == "":
            return render_template("test.html")
        elif target == "greetings":
            return redirect(url_for("greet", usr=user))
        elif target == "task1":
            return redirect(url_for("task_a", usr=user))
        elif target == "task2":
            return redirect(url_for("task_b", usr=user))
        elif target == "task3":
            return redirect(url_for("task_c", usr=user))
        elif target == "task4":
            return redirect(url_for("task_d", usr=user))
        
    else:
        return render_template("test.html")

@app.route("/<usr>")
def greet(usr):
    return f'''<h1>Hello {usr}!!</h1><br>
    <p><a href="/test"><button >BACK</button></a></p>'''

@app.route("/task1/<usr>")
def task_a(usr):
    return f'''<h1>{usr}, you are now seeing task 1 page</h1><br>
    <p>Need to wait for some time...That's your task!!</p><br>
    <a href="/test"><button >BACK</button></a>'''

@app.route("/task2/<usr>")
def task_b(usr):
    return f'''<h1>Hey {usr}, Now you are in task 2!</h1><br>
    <p>You are early here!</p>
    <p>please come back later</p>
    <a href="/test"><button >BACK</button></a>'''

@app.route("/task3/<usr>")
def task_c(usr):
    return f'''<h1>{usr}, </h1><br>
    <p>I couldn't find what to write in here!! Hope you like this</p>
    <a href="/test"><button >BACK</button></a>'''

@app.route("/task4/<usr>")
def task_d(usr):
    element = "Hi "+usr+", this is a {{ }} operator"
    return render_template("sample.html", space=element)

if __name__ == "__main__":
    app.run(debug=True)