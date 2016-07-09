from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return 'Index Page'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # do_the_login()
        return "LOGIN U BUTT"
    else:
        # show_the_login_form()
        return "GIMME YOUR LOGIN INFO"


@app.route('/hello')
def hello(name=None):
    if name is None:
        name = "Chenchenchenchenchen"
    return render_template('hello.html', name=name)


if __name__ == "__main__":
    app.run()



