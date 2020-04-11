from flask_restful import Resource, request
import json
import os

class VideoSaveData(Resource):

    def get(self):
        pass

    def post(self):

        if request.form.get('recorddate'):

            #获得数据并处理成2020(int),0402(int)的形式
            data = request.form.to_dict()
            date = data.get('recorddate')
            temp = date.split(",")
            startdate = temp[0].split("-")
            enddate = temp[1].split("-")

            startyear = int(startdate[0])
            startday = int(startdate[1] + startdate[2])
            endyear = int(enddate[0])
            endday = int(enddate[1] + enddate[2])

            #对os.walk(rootpath)下所有结果的收集以及提取需要的列表作为collect
            collectroot = []
            collect = []
            rootpath = r'/root/video/username'

            for dirs in os.walk(rootpath):
                time = dirs
                collectroot.append(time)

            for menber in collectroot:
                collect.append(menber[1])

            #初始化返回用的字典result
            result = {}
            #初始化输出元素标识以及各列表和列表指针
            resultindex = 1
            datapointer = 1
            yearlist = collect[0]
            daylist = None
            timelist = None
            yearpointer = 0
            daypointer = None
            timepointer = None
            # 进行加入操作的许可
            permission = False

            while (True):

                # 初始化daypointer
                if (daypointer is None):
                    # 若年份文件夹下不为空
                    if (len(collect[datapointer]) != 0):
                        daylist = collect[datapointer]
                        daypointer = 0
                        datapointer += 1
                    else:
                        datapointer += 1
                        yearpointer += 1
                        continue

                # 初始化timepointer
                if (timepointer is None):
                    # 若日文件夹下不为空
                    if (len(collect[datapointer]) != 0):
                        timelist = collect[datapointer]
                        timepointer = 0
                        datapointer += 1
                    else:
                        datapointer += 1
                        daypointer += 1
                        continue

                #由指针指向的时间是否在需求时间内发放permission
                if (int(yearlist[yearpointer]) >= startyear):
                    if (int(yearlist[yearpointer]) == startyear):
                        if (int(daylist[daypointer]) >= startday):
                            permission = True
                        else:
                            permission = False
                    elif (int(yearlist[yearpointer]) <= endyear):
                        if (int(daylist[daypointer]) <= endday):
                            permission = True
                        #若endyear内现日期超出范围日期，直接退出循环
                        #下方三个else可以不要
                        else:
                            break
                            permission = False
                    else:
                        permission = True
                else:
                    permission = False

                #根据permission判定是否将数据归入result
                if (permission):
                    # 不需要初始化则直接获取数据
                    # 初始化本次的取值字典
                    arrange = {}

                    # 将0402改装为-04-02
                    daystringlist = list(daylist[daypointer])
                    daystringlist.insert(0, '-')
                    daystringlist.insert(3, '-')
                    daystring = ''.join(daystringlist)

                    # 设置返回值json中第n个time（'timen'）下'date'的值
                    arrange['date'] = str(yearlist[yearpointer]) + daystring
                    arrange['minute'] = str(timelist[timepointer])
                    result['time' + str(resultindex)] = arrange

                # 指针数据的改变
                timepointer += 1
                datapointer += 1
                resultindex += 1

                # 若time指针超出timelist，则将pointer与list全部归空，重新进行初始化,并读下一个日期
                if (timepointer + 1 > len(timelist)):
                    timepointer = None
                    timelist = None
                    daypointer += 1
                    # 若day指针超出daylist，则将则将pointer与list全部归空，重新进行初始化,并读下一个年份
                    if (daypointer + 1 > len(daylist)):
                        daypointer = None
                        daylist = None
                        yearpointer += 1
                        #若year指针超出yearlist，则退出循环
                        #在上方超出endday作出break后下面的break已经失去作用
                        if (yearpointer + 1 > len(yearlist)):
                            break

                # 循环结束，结果json化
                return json.dumps(result)

        else:
            print('error')
            return "error"





