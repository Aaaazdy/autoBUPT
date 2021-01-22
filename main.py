import requests
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import logging

def autoBUPT(id='autoBUPT'):

    USERNAME = ['']#学号
    PASSWORD = ['']#信息门户密码
    FORMDATA1 = ['']
    FORMDATA2 = ['']

    #参数示例
    # USERNAME=['201XXXXXXX'] #学号
    # PASSWORD=['XXXXXXXXXX'] #信息门户密码
    #
    # FORMDATA1 = ['ismoved=0&jhfjrq=&jhfjjtgj=&jhfjhbcc=&sfxk=0&xkqq=&szgj=&szcs=&zgfxdq=0&mjry=0&csmjry=0&uid=23533&date=']  #参数一
    # FORMDATA2 = ['&tw=3&sfcxtz=0&sfyyjc=0&jcjgqr=0&jcjg=&sfjcbh=0&sfcxzysx=0&qksm=&remark=&address=%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%AE%9D%E5%B1%B1%E5%8C%BA%E7%BD%97%E5%BA%97%E9%95%87%E7%BD%97%E6%9D%9F%E8%B7%AF&area=%E4%B8%8A%E6%B5%B7%E5%B8%82++%E5%AE%9D%E5%B1%B1%E5%8C%BA&province=%E4%B8%8A%E6%B5%B7%E5%B8%82&city=%E4%B8%8A%E6%B5%B7%E5%B8%82&geo_api_info=%7B%22type%22%3A%22complete%22%2C%22position%22%3A%7B%22Q%22%3A31.412261827257%2C%22R%22%3A121.38367458767402%2C%22lng%22%3A121.383675%2C%22lat%22%3A31.412262%7D%2C%22location_type%22%3A%22html5%22%2C%22message%22%3A%22Get+ipLocation+failed.Get+geolocation+success.Convert+Success.Get+address+success.%22%2C%22accuracy%22%3A381%2C%22isConverted%22%3Atrue%2C%22status%22%3A1%2C%22addressComponent%22%3A%7B%22citycode%22%3A%22021%22%2C%22adcode%22%3A%22310113%22%2C%22businessAreas%22%3A%5B%5D%2C%22neighborhoodType%22%3A%22%22%2C%22neighborhood%22%3A%22%22%2C%22building%22%3A%22%22%2C%22buildingType%22%3A%22%22%2C%22street%22%3A%22%E6%9C%88%E6%98%A5%E8%B7%AF%22%2C%22streetNumber%22%3A%22646%E5%8F%B7%22%2C%22country%22%3A%22%E4%B8%AD%E5%9B%BD%22%2C%22province%22%3A%22%E4%B8%8A%E6%B5%B7%E5%B8%82%22%2C%22city%22%3A%22%22%2C%22district%22%3A%22%E5%AE%9D%E5%B1%B1%E5%8C%BA%22%2C%22township%22%3A%22%E7%BD%97%E5%BA%97%E9%95%87%22%7D%2C%22formattedAddress%22%3A%22%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%AE%9D%E5%B1%B1%E5%8C%BA%E7%BD%97%E5%BA%97%E9%95%87%E7%BD%97%E6%9D%9F%E8%B7%AF%22%2C%22roads%22%3A%5B%5D%2C%22crosses%22%3A%5B%5D%2C%22pois%22%3A%5B%5D%2C%22info%22%3A%22SUCCESS%22%7D&created=1609863287&sfzx=0&sfjcwhry=0&sfcyglq=0&gllx=&glksrq=&jcbhlx=&jcbhrq=&sftjwh=0&sftjhb=0&fxyy=&bztcyy=&fjsj=20200827&sfjchbry=0&sfjcqz=&jcqzrq=&jcwhryfs=&jchbryfs=&xjzd=%E5%AE%89%E5%BE%BD%E7%9C%81%E6%B7%AE%E5%8D%97%E5%B8%82%E7%94%B0%E5%AE%B6%E5%BA%B5%E5%8C%BA&sfsfbh=0&jhfjsftjwh=0&jhfjsftjhb=0&szsqsfybl=0&sfygtjzzfj=&gtjzzfjsj=&sfsqhzjkk=0&sqhzjkkys=&id=8795060&gwszdd=&sfyqjzgc=&jrsfqzys=&jrsfqzfy=']  #参数二

    url = "https://app.bupt.edu.cn/uc/wap/login?"
    resp = requests.get(url)
    eai_sess = resp.headers['Set-Cookie'].split(";")[0]

    # Login
    for i in range(len(USERNAME)):
        url2 = "https://app.bupt.edu.cn/uc/wap/login/check"
        print("start in USERNAME:" + USERNAME[i])
        print("password:" + PASSWORD[i])
        data = "username=" + USERNAME[i] + "&password=" + PASSWORD[i]
        headers = {
            "Host": "app.bupt.edu.cn",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0 micromessager",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://app.bupt.edu.cn",
            "Connection": "keep-alive",
            "Referer": "https://app.bupt.edu.cn/uc/wap/login",
            "Cookie": eai_sess
        }
        resp2 = requests.post(url2, data=data, headers=headers)
        if "操作成功" in resp2.text:
            print("登录session获取成功")
        else:
            print("登录session获取失败！")

        date = time.strftime("%Y%m%d", time.localtime())
        load_data = FORMDATA1[i] + date + FORMDATA2[i]
        url = "https://app.bupt.edu.cn/ncov/wap/default/save"
        login_cookies = eai_sess
        default_cookies = 'eai-sess=71f9l8oucr4ml62m696pgn0or6'
        headers = {
            "Host": "app.bupt.edu.cn",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0 micromessenger",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Content-Length": "2633",
            "Origin": "https://app.bupt.edu.cn",
            "Connection": "keep-alive",
            "Referer": "https://app.bupt.edu.cn/ncov/wap/default/index?from=history",
            "Cookie": login_cookies
        }
        resp = requests.post(
            url=url,
            headers=headers,
            data=load_data
        );

        # Return
        retstr = resp.text
        if "今天已经填报了" in retstr:
            print("确认填报完成。\n")
        elif "操作成功" in retstr:
            print("填报成功，随后进行确认\n")
        else:
            print("填报失败!\n")

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log1.txt',
                    filemode='a')

#windows上使用请将下一行解注释，执行函数
# autoBUPT()

scheduler = BlockingScheduler()
scheduler.add_job(func=autoBUPT,id='autoBUPT',trigger='interval',days=1,start_date='2021-01-23 00:01:00')#修改此处为下一天
scheduler._logger = logging
scheduler.start()#windows上使用请将以上四行注释
