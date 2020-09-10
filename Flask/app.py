from flask import Flask, render_template,request,redirect,url_for,session

app = Flask(__name__)

@app.route('/')
def login_form():
    return render_template('login_form.html')

#아이디,비밀번호 입력 후 연결
@app.route('/login', methods=['POST'])
def login():
    if request.method =='POST':
        if(request.form['username']=='jamie' and request.form['password']=='1234'):
            session['logged in']=True
            session['username']=request.form['username']
            return request.form['username']+"님 환영합니다."
        else:
            return '로그인 정보가 맞지 않습니다.'
    else:
        return '잘못된 접근'
    
app.secret_key ='sample_secret_key'

@app.route('/get_test', methods=['GET'])
def get_test():
    if request.method=='GET':
        if(request.args.get('username')=="jamie" and request.args.get('password')=="1234"):
            return request.args.get('username')+ "님 환영합니다."
        else:
            return '로그인 정보가 맞지 않습니다.'
    else:
        return '잘못된 접근'
    
   
@app.route('/logout')
def logout():
    session['logged_in']=False
    session.pop('username',None)
    return redirect(url_for('login_form')) #해당페이지로 이


#서버 연결
if __name__ == '__main__':
   app.run()