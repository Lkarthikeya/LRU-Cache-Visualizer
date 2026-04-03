from flask import Flask, render_template, request, redirect
from cache import LRUCache

app = Flask(__name__)

cache = LRUCache(3)


@app.route("/")
def home():
    return render_template(
        "index.html",
        cache=cache.get_cache(),
        stats=cache.stats(),
        logs=cache.logs
    )


@app.route("/put", methods=["POST"])
def put():
    key = request.form.get("key")
    value = request.form.get("value")

    if key and value:
        cache.put(key, value)

    return redirect("/")


@app.route("/get", methods=["POST"])
def get():
    key = request.form.get("getKey")

    if key:
        cache.get(key)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)