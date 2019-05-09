# myflask file

from flask import Flask, render_template
import time
import config

app = Flask(__name__)


@app.route('/')
def hello_world():
    a=1
    b=0
    c=a/b
    #time.sleep(5)
    name='你浩哥'
    return render_template('index.html',name=name)

if __name__ == '__main__':
    app.run()
