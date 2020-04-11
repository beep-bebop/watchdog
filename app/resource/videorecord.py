from flask_restful import Resource, request
from flask import Response
import cv2

picturecounter = 1


class VideoRecord(Resource):


    def get(self):
        pass

    def post(self):
        global picturecounter

        if request.form.get('picturedate') and request.form.get('time'):
            data = request.form.to_dict()
            date = data.get('picturedate')
            temp = date.split("-")
            year = temp[1]
            day = temp[2]

            data = request.form.to_dict()
            picpath = r'/root/video/username/%s/%s/%s' % (year, day, data.get('time'), str(picturecounter))
            picturecounter += 1
            if(picturecounter > 5):
                picturecounter = 1
                return False

            image = cv2.imread(picpath)

            bs = cv2.imencode(".jpg", image)[1].tobytes()

            return Response(bs, mimetype='image/jpeg')

        else:
            print('error')
            return "error"





