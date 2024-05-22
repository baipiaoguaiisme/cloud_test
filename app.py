from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '谭老师真的很耀眼！'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
