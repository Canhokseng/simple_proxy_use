#小幻代理爬取
import requests
from bs4 import BeautifulSoup

url="https://ip.ihuan.me/address/5Lit5Zu9.html"
headers={
    'Host': 'ip.ihuan.me',
    'Cookie': 'Hm_lvt_8ccd0ef22095c2eebfe4cd6187dea829=1708056810,1708077269,1708145834; cf_chl_3=3f21092ac79f57e; cf_clearance=SUNJT6RCbyRCv_gx79p0Xrk6rvis8wBPn9iOfgb_2IY-1708152740-1.0-ATNJhWOwg/tK40zJ9yzys0XslCNPe0qDMOWoVTrctsG3RHkGcLs/TfGVAew2/x+gL5QKfPc2+RW/CjBL2Llbub4=; Hm_lpvt_8ccd0ef22095c2eebfe4cd6187dea829=1708152758',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Sec-Ch-Ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Full-Version': '"121.0.2277.112"',
    'Sec-Ch-Ua-Arch': '"x86"',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Ch-Ua-Platform-Version': '"10.0.0"',
    'Sec-Ch-Ua-Model': '""',
    'Sec-Ch-Ua-Bitness': '"64"',
    'Sec-Ch-Ua-Full-Version-List': '"Not A(Brand";v="99.0.0.0", "Microsoft Edge";v="121.0.2277.112", "Chromium";v="121.0.6167.160"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://ip.ihuan.me/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'close',

}
resp=requests.post(url,headers=headers)

#将text爬虫文本格式化
soup=BeautifulSoup(resp.text,'html.parser')
tables=soup.find_all('table')
tab=tables[0]
ports=[]
ips=[]

for tr in tab.tbody.find_all('tr'):
  for index, td in enumerate(tr.findAll('td')):
    if index == 0:
        ip = td.find('a').text
        ips.append(ip)
    if index == 1:
        port = td.getText()
        ports.append(port)
    if index == 4:
        support_https = td.getText()
    if index == 5:
        support_post = td.getText()
    if index == 7:
        speed = td.getText().replace('秒', '')

cnt=0
#对网站进行目录扫描
test_headers={
    'Host': 'menovopharm.com',
    'Cookie': '_ga=GA1.2.1323643342.1697879918; _ga_0D69GQCMCK=GS1.2.1697879918.1.0.1697879918.0.0.0; PHPSESSID=fud8utebfio34t08i9aqmehra0; _gat=1',
    'Sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
    'Sec-ch-ua-mobile': '?0',
    'Sec-ch-ua-platform': '"Windows"',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'close'
}
for paths in open('php.txt', encoding='utf-8'):
    url = "https://menovopharm.com/"
    paths = paths.replace('\n', '')
    urls = url + paths
    proxy = {
        'http': 'http://{}:{}'.format(ips[cnt],ports[cnt])
    }
    try:
        code = requests.get(urls, headers=test_headers, proxies=proxy).status_code
        # time.sleep(3)
        if code == 200 or code==403:
          print(urls + '|' + str(code))
    except Exception as err:
        print('connect error')
    cnt+=1
    if cnt>=len(ips):
        cnt%=len(ips)