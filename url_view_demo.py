from flask import Flask,request
import config

app=Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello():
    return 'hello haoge'

@app.route('/article/<int:article_id>')
def article(article_id):
    return '您请求的文章是%s' % article_id

@app.route('/test/<path:test>')
def test(test):
    return '您请求的是%s '% test

@app.route('/test1/<float:test>')
def test1(test):
    return '您请求的是%s '% test

@app.route('/test2/<string:test>')
def test2(test):
    return '您请求的是%s '% test

@app.route('/user/<uuid:user_id>')
def user(user_id):
    return '您请求的是%s' % user_id

import uuid
print(uuid.uuid4())

@app.route('/<any(blog,text):url_path>/<id>')
def detail(url_path,id):
    if url_path=='blog':
        return '博客详情:%s' % id
    else:
        return '用户详情：%s' % id

@app.route('/que/')
def que():
    wd=request.args.get('wd')
    return '您通过查询字符串的参数是(%s)'% wd

if __name__=='__main__':
    app.run()

