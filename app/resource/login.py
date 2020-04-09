from flask_restful import Resource, request
from ..util.dbutil import sign_in

class Login(Resource):
    def get(self):
        pass

    def post(self):
        if request.form.get('username') and request.form.get('password'):
            data = request.form.to_dict()
            username = data.get("username")
            password = data.get("password")
            print(username,password)
            res = sign_in(username, password)
            print("res:"+str(res))
            if res == 0 and username == "admin" :
                return "admin"
            else :
                return res
        else :
            print("error")
            return "error"