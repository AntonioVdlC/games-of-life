import os

from flask import (
    Flask,
    make_response,
    send_from_directory,
    render_template,
    redirect,
    url_for,
    jsonify,
    request,
)
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder="views", static_folder="www/dist")

# App Routes
@app.route("/")
def root():
    return redirect(url_for("new"))


@app.route("/new")
def new():
    return render_template("new.html")


@app.route("/u")
def universe():
    id = request.args.get("id")
    if id == None:
        return redirect(url_for("new"))

    return render_template("universe.html", id=id)


# API
@app.route("/api/universe/<id>", methods=["GET"])
def get_universe(id):
    # TODO
    return jsonify(id=id)


@app.route("/api/universe", methods=["POST"])
def create_universe():
    # TODO
    return jsonify(id="TODO")


# Static files
@app.route("/<path:path>")
def static_file(path):
    mimetypes = {
        ".html": "text/html",
        ".css": "text/css; charset=utf-8",
        ".js": "application/javascript; charset=utf-8",
        ".wasm": "application/wasm",
    }
    extension = "." + path.split(".")[-1]

    r = make_response(send_from_directory("www/dist", path))
    r.mimetype = mimetypes.get(extension)

    return r


if __name__ == "__main__":

    # set the absolute path to the static folder
    app.static_url_path = "/www/dist"
    app.static_folder = app.root_path + app.static_url_path

    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

