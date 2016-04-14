from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "super secret key"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/udp')
def udp():
	mess = "test"
	return render_template('udptest.html',mess=mess)


if __name__ == '__main__':
    from werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(host='0.0.0.0',debug=True)
