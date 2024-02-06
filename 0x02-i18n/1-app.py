#!/usr/bin/env python3
"""0x02. i18n"""


from flask import Flask, render_template
from flask_babel import Babel


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = "en"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route("/", methods=["GET"])
def home():
    """default home page"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
