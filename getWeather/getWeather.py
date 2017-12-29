#-*- coding:utf-8 -*- 
import sys 
import json
from urllib.request import urlopen

def getWeather(location):
    # 获取天气的api为和风天气
    # https://www.heweather.com/
    url = 'https://free-api.heweather.com/s6/weather/now?location=' + location +'&key=4fb0326229654f0ea27fa734e745ee0d'
    page = urlopen(url)
    data_json = page.read().decode("utf-8")
    data_dic = json.loads(data_json)
    content = data_dic["HeWeather6"][0]
    if (content["status"] == 'ok'):
        basic = content["basic"]
        now = content["now"]
        update = content["update"]
        print("你所查询的位置:" + basic["location"])
        print("天气:" + now["cond_txt"])
        print("体感温度:" + now["fl"] + "摄氏度")
        print("温度:" + now["tmp"] + "摄氏度")
        print("气压:" + now["pres"])
        print("降水量:" + now["pcpn"])
        print("能见度:" + now["vis"] + "公里")
        print("风力:" + now["wind_sc"])
        print("风向:" + now["wind_dir"])
        print("风速:" + now["wind_spd"] + "公里/小时")
        print("更新自:" + update["loc"])
    else:
        print('获取天气失败！')

def main():
    # location 示例:
    # location = 北京 | beijing | CN101010100 | 60.194.130.1 | 120.343,36.088
    if (len(sys.argv) < 2):
        print("请输入要查询的地址!")
    for args in sys.argv[1:]:
        getWeather(args)

if __name__ == '__main__':
    main()

