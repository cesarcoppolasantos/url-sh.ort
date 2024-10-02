import os

from flask import Flask, redirect, render_template, url_for, request, session
from short_urls import store_urls, get_long_url, create_json


app = Flask(__name__)
app.secret_key = os.urandom(24)


def ensure_https(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'https://' + url  # ou http:// dependendo do caso
    return url


@app.route('/')
def home():
    return render_template('create_url.html')


@app.route('/submit', methods=["POST"])
def create_short_url():

    long_url = request.form['long_url']
    short_url = store_urls(long_url)
    session['short_url'] = short_url

    return redirect(url_for('new_url'))


@app.route('/<short_url>')
def redirect_to_long_url(short_url):

    long_url = get_long_url(short_url)

    if long_url:
        long_url = ensure_https(long_url)
        return redirect(long_url)
    else:
        return "URL not found.", 404
    
    
@app.route('/new_url')
def new_url():

    short_url = session.get('short_url')
    long_url = get_long_url(short_url)
    long_url = ensure_https(long_url)

    return render_template('new_url.html', short_url=f"sh.ort/{short_url}", long_url=long_url)


if __name__ == "__main__":
    create_json()
    app.run(debug=True, host='0.0.0.0', port=80)

