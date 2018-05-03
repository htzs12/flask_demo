from flask import Flask,url_for
import config

app=Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/user/<int:user_id>')
def user_profile(user_id):
    return '您输入的id为：' % user_id

if __name__ == '__main__':
    app.run()