# !/usr/bin/env python3
"""0x02. i18n"""


from flask import Flask, render_template

# from flask_babel import Babel

app = Flask(__name__)

# babel = Babel()
# babel.init_app(app)


@app.route("/", methods=["GET"])
def home():
    """home page"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
