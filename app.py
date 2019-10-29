import os

from flask import Flask, make_response, send_from_directory
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/")
def root():
    return app.send_static_file("index.html")


@app.route("/<path:path>")
def static_file(path):
    mimetypes = {
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

