from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    data = request.json
    headers = {
        'accept':
        'application/json, text/plain, */*',
        'accept-language':
        'en-US,en;q=0.9,hi;q=0.8',
        'cache-control':
        'no-cache',
        'content-type':
        'application/json',
        'user-agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }
    response = requests.post('https://cardgpt.in/apitest',
                             headers=headers,
                             json=data)
    return jsonify(response.json())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
