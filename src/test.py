import json
import urllib.request

http="http://api.k780.com"                   #接口网址

appkey="34456"                                #AppKey,Sign
sign="56a6d73b4e319771c288aa793e4fee0b"

f=open("H:\\tty3.py","w")                   #文件指针

url=("%s/?app=weather.city&appkey=%s&sign=%s&cou=1&format=json"%(http,appkey,sign))
http_data=urllib.request.urlopen(url).read().decode("utf-8")
json_data=json.loads(http_data)
js1=json_data["result"]
city={}
for value in js1.values():
    citynm=str(value["citynm"])
    cityid=str(value["cityid"])
    city[citynm]=cityid
stri="city={"
for key in city.keys():
    stri=stri+"%s:%s,\n"%(key,city[key])

stri+="}"
f.write(stri)
f.close()


