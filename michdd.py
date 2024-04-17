
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/links', methods=['GET'])
def get_links():
    with open('links.json') as f:
        links = json.load(f)
    return render_template('links.html', links=links)

if __name__ == '__main__':
    app.run()
