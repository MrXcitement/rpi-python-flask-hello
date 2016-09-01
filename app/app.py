from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    html = "<h1>Hello World!</h1>"
    html += "<hr>"
    html += "<p>"
    html += "A simple hello world web app, in a docker image, "
    html += "using debian, python and flask!"
    html += "</p>"
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
