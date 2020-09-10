#!/user/bin/python
# -*- coding: utf-8 -*-

from flask import Flask,url_for
app=Flask(__name__)

@app.route('/')
def hello_world():
     return 'Hello World'

@app.route('/main')
def main():
     return 'main page'


@app.route('/user/<username>')
def show_user_profile(username):
     return 'User %s' % username

if __name__=='__main__':
    #test_request_context()함수를 사용하여 url_for함수에서 반환되는 url을 확인
    with app.test_request_context():
        print(url_for('show_user_profile', username='flask'))
        app.run()


@app.route('/post/<int:post_id>')
def show_post(post_id):
     return 'Post %d' % post_id

@app.route('/logging')
def logging_test():
      test=1
      app.logger.debug('디버깅 필요')
      app.logger.warning(str(test) +"라인")
      app.logger.error('에러발생')
      return "로깅 끝"

