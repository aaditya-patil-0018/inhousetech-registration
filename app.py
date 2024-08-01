from flask import Flask
from flask import render_template
from flask import request
from database import DB

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "GET":
        return render_template("main.html")
    else:
        fname = request.form.get('first-name')
        lname = request.form.get('last-name')
        phn = request.form.get('contact-number')
        email = request.form.get('email')

        db = DB()
        db.update(fname, lname, phn, email)

        return "Thank you for Registration"

if __name__ == "__main__":
    app.run(debug=True)