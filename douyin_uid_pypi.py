# _*_ encoding = utf-8 _*_
# @Time   :2023/9/20 9:40
# @Author :caohui 
# @Email  :408141249@qq.com
import requests,re
import urllib.parse

class douyinuid:
    def __init__(self):
        self.url = ''
        self.Cookie = ''

    def GetDouYinId(self):
        headers = {
            'authority': 'www.douyin.com',
            'method': 'GET',
            'path': '/user/MS4wLjABAAAAoPT3QS8YxUdQuBbGSUENF_1pguAynWAnjiqfpB0V3XQ?vid=7274267955251186980',
            'scheme': 'https',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Cookie': f'{self.Cookie}',
            'Sec-Ch-Ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': 'Windows',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        }
        res = requests.get(self.url, headers=headers).text
        res1 = re.findall('id="RENDER_DATA" type="application/json">(.*?)</script>', res)[0]
        return res1

    # 查询
    def handle(self):
        try:
            res = self.GetDouYinId()
            # 将返回的数据使用url解码
            url_decode = urllib.parse.unquote(res)
            # print(url_decode)
            uid = re.findall('"uid":"(.*?)"', url_decode)[1]
            nickname = re.findall('"nickname":"(.*?)"', url_decode)[1]
            return f'抖音用户"{nickname}"userID:{uid}'
        except:
            return f'用户url或cookie值错误，请确认后再重新查询...'
