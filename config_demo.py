from flask import  Flask
import config

app=Flask(__name__)
app.config.from_object(config)
#app.config.from_pyfile('config.py')

@app.route('/')
def index():
    return 'hello'

if __name__ == '__main__':
    app.run()