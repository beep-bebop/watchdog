from flask_restful import Resource, request
from ..util.dbutil import sign_up

class Register(Resource):
    def get(self):
        pass

    def post(self):
        if request.form.get('username') and request.form.get('password') :
            data = request.form.to_dict()
            username = data.get("username")
            password = data.get("password")
            phonenum = data.get("phonenum")
            dorm = data.get("dorm")
            room = data.get("room")
            print("register:"+username+password)
            res = sign_up(username,password,phonenum,dorm,room)
            print("res:"+str(res))
            return res
        else :
            print("error")
            return "error"