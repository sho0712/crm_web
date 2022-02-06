from flask import Flask, render_template, request, redirect, url_for

import db

app = Flask(__name__)


# /にGETでアクセスが来たらindex.htmlを返す
@app.get("/")
def index():
    customers = db.get_all_customers()
    return render_template("index.html", customers=customers)


@app.post("/")
def register():
    place = request.form['place']
    temp = request.form['temp']
    db.add_customer(place, temp)

    # 処理が終わったら（）に移動する　行き先を指定できる
    # return redirect("/index")
    # index関数に移動してください。
    return redirect(url_for("index"))


if __name__ == '__main__':
    port = 5000
    app.run(port=port, debug=True)
