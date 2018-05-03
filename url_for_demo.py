from flask import Flask,url_for
import config

app=Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello_world():
    print(url_for('my_list',page=1,count=2,next='/'))
    return 'hello world'

@app.route('/list/<page>/')
def my_list(page):
    return 'hello world'

if __name__ == '__main__':
    app.run()