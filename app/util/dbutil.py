import pymysql
import re

db = pymysql.connect("rm-2ze61i7u6d7a3fwp9yo.mysql.rds.aliyuncs.com", "team", "Aaa5225975", "pidata")
cursor = db.cursor()

def add_single_data(json_data):
    sql = "insert into sensors(data) values('%s')" % (json_data)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    print(sql)

def add_warning_data(json_data):
    sql = "insert into warning(data) values('%s')" % (json_data)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    print(sql)

def sign_in(username, password):
    sql = "select password from signon where username=\'"+username+"\'"
    cursor.execute(sql)
    row = cursor.fetchone()
    if not row :
        return -1 #未注册
    if str(row[0]) == password :
        return 1 #登陆成功
    return 0 #密码错误

def sign_up(username, password, phonenum, dorm, room):
    sql = "select password from signon where username=\'"+username+"\'"
    cursor.execute(sql)
    row = cursor.fetchone()
    if row :
        return -1 #该用户名已注册
    if not re.match("^1(3[0-9]|4[579]|5[0-3,5-9]|6[6]|7[0135678]|8[0-9]|9[89])\d{8}$", phonenum) :
        return 0 #手机号不合法
    sql1 = "insert into signon(username, password) values('%s', '%s')" % (username, password)
    sql2 = "insert into user(username, identity, phonenum, dorm, room) values('%s', 'costumer', '%s', '%s', '%s')" \
        % (username, phonenum, dorm, room)
    try:
        cursor.execute(sql1)
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        return -2
    return 1
    
    
