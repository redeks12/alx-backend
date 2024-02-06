# !/usr/bin/env python3
"""0x02. i18n"""


from flask import Flask, render_template
from flask_babel import Babel


class Config:
    LANGUAGES = ["en", "fr"]
    TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()
babel.init_app(
    app,
    default_locale=app.config["LANGUAGES"][0],
    default_timezone=app.config["TIMEZONE"],
)


@app.route("/", methods=["GET"])
def home():
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
