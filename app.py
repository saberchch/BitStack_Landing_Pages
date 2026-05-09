# pyrefly: ignore [missing-import]
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/token')
def token():
    return render_template('token.html')

@app.route('/mentors')
def mentors():
    return render_template('mentors.html')

@app.route('/learners')
def learners():
    return render_template('learners.html')

@app.route('/freelancers')
def freelancers():
    return render_template('freelancers.html')

@app.route('/institutes')
def institutes():
    return render_template('institutes.html')

@app.route('/clients')
def clients():
    return render_template('clients.html')

@app.route('/library')
def library():
    return render_template('library.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/join')
def join():
    return render_template('join.html')

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/<path:path>')
def placeholder(path):
    return render_template('placeholder.html', path=path)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
