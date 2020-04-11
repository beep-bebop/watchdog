from flask_restful import Resource
from flask import json, Response, send_file
import imagezmq
import cv2
import datetime
import numpy as np
import os
import imagezmq

imagehub = imagezmq.ImageHub()
background = None
text = "no target"
timeIndex = 1
target = False  # 是否存在标记，作为是否保存的标识之一
frequencecounter = 0  # 保存总次数
repeatavoidcounter = 0  # 防止重复保存的标识之一
picturecounter = 0  # 防止过多记录的标识

class Video(Resource):

    #如果方法为get 调用该方法
    def get(self):
        global imagehub,background,text,timeIndex,target,frequencecounter,repeatavoidcounter,picturecounter

        # print('in circulation')
        rpi_name, jpg_buffer = imagehub.recv_jpg()
        # np.frombuffer将缓冲区变成一维数组;imdecode读取数据解码成图像格式
        image = cv2.imdecode(np.frombuffer(jpg_buffer, dtype='uint8'), -1)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)  # 括号内值越高越模糊，不能为偶数
        # 将第一帧设置为整个输入的背景
        if background is None:
            background = gray
            imagehub.send_reply(b'OK')
            bs = cv2.imencode(".jpg", image)[1].tobytes()
            repeatavoidcounter += 1
            timeIndex += 1
            return Response(bs, mimetype='image/jpeg')

        if timeIndex % 20 == 0:
            background = gray
        # 当前帧和第一帧的不同它可以把两幅图的差的绝对值输出到另一幅图上面来
        frameDelta = cv2.absdiff(background, gray)
        # 二值化
        thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
        # 腐蚀膨胀
        thresh = cv2.dilate(thresh, None, iterations=2)
        # 取轮廓
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)[-2]
        # 遍历轮廓
        for c in cnts:
            if cv2.contourArea(c) < 1800:  # 对于较小矩形区域，选择忽略
                continue
            flat = 1  # 设置一个标签，当有运动的时候为1
            # 计算轮廓的边界框，在当前帧中画出该框
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            text = "Find Target"
            target = True
            # print("Find Target!")
        cv2.putText(image, text, (10, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.putText(image, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                    (10, image.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

        # 找到目标
        if (target):
            # 保存冷却完毕
            target = False
            repeatstr = '%d' % repeatavoidcounter
            picturestr = '%d' % picturecounter
            frequencestr = '%d' % frequencecounter
            print("repeat: " + repeatstr + " pic: " + picturestr + " frequent: ", frequencestr)
            if (repeatavoidcounter > 30):
                year = datetime.datetime.now().strftime("%Y")
                day = datetime.datetime.now().strftime("%m%d")
                minute = datetime.datetime.now().strftime("%H%M")

                if (picturecounter < 5):
                    picturecounter += 1
                    # 需被创建的保存路径
                    path = 'C:\\Users\\Y\\Desktop\\project\\username\\' + year + '\\' + day + '\\' + minute
                    #path = r'/root/video/username/%s/%s/%s' % (year, day, minute)

                    # 保存
                    if not os.path.exists(path):
                        os.makedirs(path)
                    print('unchanged:' + path)
                    # 图片路径
                    picpath = r'C:\Users\Y\Desktop\project\username\%s\%s\%s\%s.jpg' % (year, day, minute, picturestr)
                    # picpath = r'/root/video/username/%s/%s/%s/%s.jpg' % (year, day, minute,picturecounter)
                    cv2.imwrite(picpath, image)
                    # print("writing done")
                else:
                    repeatavoidcounter = 0
                    picturecounter = 0
                    frequencecounter += 1

        bs = cv2.imencode(".jpg", image)[1].tobytes()
        imagehub.send_reply(b'OK')
        repeatavoidcounter += 1
        timeIndex += 1

        return Response(bs, mimetype='image/jpeg')


    def post(self):
        print("post")