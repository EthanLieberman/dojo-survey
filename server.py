from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'test'


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit_form', methods=['post'])
def submit_form():
    session['name'] = request.form['name']
    session['language'] = request.form['language']
    session['favorite_food'] = request.form['favorite_food']
    return redirect("/userinfo")

@app.route('/userinfo')
def userinfo():
    return render_template('userinfo.html')




if __name__ == "__main__":
    app.run(debug=True)