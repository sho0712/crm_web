from flask import Flask, render_template, request

import db

app = Flask(__name__)


# /indexにGETでアクセスが来たらindex.htmlを返す
@app.get("/index")
def index():
    customers = db.get_all_customers()
    return render_template("index.html", customers=customers)


@app.post("/index")
def register():
    name = request.form['name']
    age = request.form['age']
    db.add_customer(name, age)

    return render_template("index.html")


if __name__ == '__main__':
    port = 5000
    app.run(port=port, debug=True)
