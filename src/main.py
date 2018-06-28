import urllib.request
import json
from city import city_list

def pri_weather(weat_data):      #结果输出
    print("日期：%s月%s日 %s"%(weat_data['month'],weat_data['day'],weat_data["week"]))
    print("气温：%s" % weat_data['temperature'])
    print("湿度：%s" % weat_data['humdity'])
    print("天气：%s" % weat_data['weather'])
    print("风向：%s" % weat_data['wind'])
    print("风速：%s" % weat_data['winp'])

def urlrequ(app,cityid):
    http = "http://api.k780.com"  # 接口网址
    appkey = "34456"  # AppKey
    sign = "56a6d73b4e319771c288aa793e4fee0b" # Sign
    url = ("%s/?app=weather.%s&weaid=%s&appkey=%s&sign=%s&format=json" % (http, app, cityid, appkey, sign))  # url拼接
    http_callback = urllib.request.urlopen(url=url, data=None, timeout=10).read().decode("UTF-8")  # http返回
    json_callback = json.loads(http_callback)["result"]  # 处理json数据,得到结果集
    return json_callback


cityname=input("请输入城市：")

cityid=city_list.get(cityname)
today_data=urlrequ("today",cityid)
fut_data=urlrequ("future",cityid)
print("今日天气：")
weat_data={}                                       #结果集整理
weat_data['month']=today_data["days"].split("-")[1]     #月份
weat_data['day']=today_data["days"].split("-")[2]        #日期
weat_data['week']=today_data["week"]                     #星期
weat_data['temperature']=today_data["temperature"]      #气温
weat_data['humdity']=today_data["humidity"]             #湿度
weat_data['weather']=today_data["weather"]              #天气
weat_data['wind']=today_data["wind"]                    #风向
weat_data['winp']=today_data["winp"]                    #风速
pri_weather(weat_data)
print("未来天气:")
for i in range(1,4):
    weat_data={}                                       #结果集整理
    weat_data['month']=fut_data[i]["days"].split("-")[1]     #月份
    weat_data['day']=fut_data[i]["days"].split("-")[2]        #日期
    weat_data['week']=fut_data[i]["week"]                     #星期
    weat_data['temperature']=fut_data[i]["temperature"]      #气温
    weat_data['humdity']=fut_data[i]["humidity"]             #湿度
    weat_data['weather']=fut_data[i]["weather"]              #天气
    weat_data['wind']=fut_data[i]["wind"]                    #风向
    weat_data['winp']=fut_data[i]["winp"]                    #风速
    pri_weather(weat_data)







