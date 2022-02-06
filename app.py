from flask import Flask, render_template

app = Flask(__name__)


# /indexにGETでアクセスが来たらindex.htmlを返す

@app.route("/index")
def index():

    customers = [["bob", 15],
                 ["Tom", 57],
                 ["Ken", 73]]

    return render_template("index.html", customers=customers)


if __name__ == '__main__':
    port = 5000
    app.run(port=port, debug=True)
