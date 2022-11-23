from flask import Flask,jsonify,render_template,redirect, request, url_for, flash, session
from  settings import Config,host,username,password,port,db
app=Flask(__name__)
app.config.from_object(Config)
from utils.MySQL import MysqlHelper
from functools import wraps
mydb=MysqlHelper(host=host,db=db,username=username,password=password,port=port)
def is_login(func):
    @wraps(func)
    def inner(*args,**kwargs):
        user = session.get('user')
        if not user:
            return redirect(url_for('login'))
        return func(*args,**kwargs)
    return inner
@app.route('/',methods=['GET'])
@is_login
def index():
    return redirect('/park/summary')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form,request.values)
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        sql = "select username from users where username='{}' and password='{}'".format(username,password)
        print(sql)
        flag = len(mydb.get_all(sql))
        if flag:
            # session['user'] = username
            # return redirect(url_for('index'))
            return jsonify({'code':200,'msg':'User login successfully.'})
        else:
            # a pop-up appears:
            # flash('%sUsername or password is wrong, please retry again....' % (username))
            # return redirect(url_for('login'))
            return jsonify({'code': 400, 'msg': 'User login failed.'})
    return render_template('login.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        sql = "select username from users where username='{}'".format(username)
        flag=len(mydb.get_all(sql))
        # when all the info in park.users has been traversed and no registered user is found, the current user name is added to the table and it’ll automatically jump to the summary page
        if flag:
            return render_template('register.html', messages='User %s already existed.' % username)
        else:
            sql="insert into users(username,password) select '{}','{}'".format(username,password)
            # users.append(dict(username=username, password=password))
            mydb.insert(sql)
            # a pop-up appears:
            flash('The user %s has successfully registered，please login.....' % username, category='info')
            return redirect(url_for('login'))

    return render_template('register.html')
@app.route('/parkjson',methods=['GET','POST'])
# @is_login
def parkjson():
    sql='select * from parkspot'
    data=mydb.get_all(sql)
    info = request.values
    limit = info.get('limit', 10)  # lines in every page
    offset = info.get('offset', 0)  # the starter of the data in one page, (page-1)*limit
    ccode = info.get('ccode','')
    if  ccode:
        sql="select * from parkspot where vchiclecode='{}'".format(ccode)
        data=mydb.get_all(sql)
    return jsonify({'total': len(data), 'rows': data[int(offset):(int(offset) + int(limit))]})
@app.route('/park',methods=['GET','POST'])
# @is_login
def park():
    return render_template('parklist.html')

@app.route('/api/park/avail',methods=['GET','POST'])
# @is_login
def queryavail():
    sql="select * from parkspot where vchiclecode is null"
    data=mydb.get_all(sql)
    print(data)
    info = request.values
    limit = info.get('limit', 10)  # lines in every page
    offset = info.get('offset', 0)  # the starter of the data in one page, (page-1)*limit
    return jsonify({'total': len(data), 'rows': data[int(offset):(int(offset) + int(limit))]})

@app.route('/park/avail',methods=['GET','POST'])
# @is_login
def parkavail():
    return render_template('avaliable.html')

@app.route('/api/park/summary',methods=['GET','POST'])
# @is_login
def querysummary():
    sql="select distinct area,areacode,allspot,avaliable from parkspot"
    data=mydb.get_all(sql)
    print(data)
    info = request.values
    limit = info.get('limit', 10)  # lines in every page
    offset = info.get('offset', 0)  # the starter of the data in one page, (page-1)*limit
    return jsonify({'total': len(data), 'rows': data[int(offset):(int(offset) + int(limit))]})

@app.route('/park/summary',methods=['GET','POST'])
# @is_login
def parksummary():
    return render_template('summary.html')

@app.route('/api/park/use',methods=['GET','POST'])
# @is_login
def queryuse():
    sql="select * from parkspot where vchiclecode is not null"
    data=mydb.get_all(sql)
    info = request.values
    limit = info.get('limit', 10)  # lines in every page
    offset = info.get('offset', 0)  # the starter of the data in one page, (page-1)*limit
    return jsonify({'total': len(data), 'rows': data[int(offset):(int(offset) + int(limit))]})

@app.route('/park/use',methods=['GET','POST'])
# @is_login
def parkuse():
    return render_template('use.html')

@app.route('/park/release',methods=['GET','POST'])
# @is_login
def release():
    print(request.form)
    id=request.form.get('id','')
    ccode1=request.form.get('ccode1','')
    pcode1 = request.form.get('pcode1', '')
    areacode1 = request.form.get('areacode1', '')
    id=int(id)
    sql="select id from parkspot where id={} and vchiclecode is not null".format(id)
    print(sql)
    cnt=len(mydb.get_all(sql))
    print(cnt)
    if cnt>0:
        sql="update parkspot set vchiclecode=null where id={};update parkspot set avaliable=avaliable+1 where areacode='{}';".format(id,areacode1)
        print(sql)
        mydb.update(sql)
        return jsonify({'code':200,'msg':'Cancelled successfully.'})
    return jsonify({'code':404,'msg':'Cancel failed.'})
@app.route('/park/bus',methods=['GET','POST'])
# @is_login
def bus():
    id = request.form.get('id', '')
    ccode2=request.form.get('ccode2','')
    pcode2 = request.form.get('pcode2', '')
    areacode2 = request.form.get('areacode2', '')
    print(type(id),id)
    id = int(id)
    sql = "select id from parkspot where id={} and vchiclecode is  null".format(id)
    print(sql)
    cnt = len(mydb.get_all(sql))
    print(cnt)
    if cnt > 0:
        sql = "update parkspot set vchiclecode='{}' where id={};update parkspot set avaliable=avaliable-1 where areacode='{}';".format(ccode2,id,areacode2)
        print(sql)
        mydb.update(sql)
        return jsonify({'code':200,'msg':'Parked successfully.'})
    else:
        return jsonify({'code':404,'msg':'The current parking spot is not available.'})

@app.route('/park/reload',methods=['GET','POST'])
# @is_login
def reload():
    print(request.form)
    id = request.form.get('id', '')
    ccode3=request.form.get('ccode3','')
    opcode3 = request.form.get('opcode3', '')
    npcode3 = request.form.get('npcode3', '')
    areacode3 = request.form.get('areacode3', '')
    sql = "select id from parkspot where parkcode='{}' and vchiclecode is  null".format(npcode3)
    print(sql)
    cnt = len(mydb.get_all(sql))
    print(cnt)
    if cnt>0:
        sql="update parkspot set vchiclecode=null where parkcode='{}' and areacode='{}';update parkspot set vchiclecode='{}' where parkcode='{}' and areacode='{}';".format(opcode3,areacode3,ccode3,npcode3,areacode3)
        print(sql)
        mydb.update(sql)
        return jsonify({'code': 200, 'msg': 'Changed parking spot successfully.'})
    else:
        return jsonify({'code': 404, 'msg': 'Change parking spot failed.'})
@app.route('/logout',methods=['GET','POST'])
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__=='__main__':
    app.run(host='127.0.0.1',debug=True,threaded=True)
