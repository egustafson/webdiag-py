import datetime
import subprocess

from flask import Flask, render_template_string

template = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>ts: {{ ts }}</p>
    <pre>{{ results }}</pre>
</body>
</html>
"""


app = Flask(__name__)
app.config.from_pyfile('../config.py')

@app.route('/')
def index():
    return {
        "status": "ok",
        "ts": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

@app.route('/arp')
def arp():
    ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    results = subprocess.run(['arp', '-a'], capture_output=True, text=True)
    return render_template_string(template, title="ARP Table", ts=ts, results=results.stdout)

@app.route("/ifconfig")
def ifconfig():
    ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    results = subprocess.run(['ifconfig', '-a'], capture_output=True, text=True)
    return render_template_string(template, title="ifconfig", ts=ts, results=results.stdout)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
