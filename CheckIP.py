# -*- coding: utf-8 -*-
import requests
import os

# 脚本自動識別當前目錄下的 IPS.txt 文件，若不存在則手動輸入文件夾路徑，注意：路徑後面需要加 /
# 獲取cloudflare的反代IP，保存到 Success_IPS.txt 中
# 獲取失敗的IP，保存到 Fail_IPS.txt 中
# 探測失敗的IP，保存到 Continue_IPS.txt 中

# 保存文件路徑
Success_PATH = os.getcwd() + '/Success_IPS.txt'
Fail_PATH = os.getcwd() + '/Fail_IPS.txt'
Continue_PATH = os.getcwd() + '/Continue_IPS.txt'
Index_PATH = os.getcwd() + '/Index.txt'


timeout = float(input('請輸入每個IP超時時間：'))
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

# 檢測IP文件
if not os.path.exists('IPS.txt'):
    IPS_PATH = input('檢測不到 IPS.txt 文件，請手動輸入文件夾路徑：')
    # 文件夾下讀取探測
    for file in os.listdir(IPS_PATH):

        file = IPS_PATH + file
        print('正在讀取:' + file)
        with open(file, 'r') as f:
            IPLIST = f.readlines()
            for IP in IPLIST:
                IP = IP.strip()
                URL = 'http://' + IP + '/cdn-cgi/trace'

                # 寫入當前探測的IP
                with open(Index_PATH, 'w') as i:
                    i.write(IP)

                try:
                    res = requests.get(URL, headers, timeout=timeout).text
                except:
                    print('continue:' + IP)
                    with open(Continue_PATH, 'a+') as t:
                        t.write(IP + '\n')
                    continue

                if 'tls' in res:
                    print('Success:' + IP)
                    with open(Success_PATH, 'a+') as t:
                        t.write(IP + '\n')
                else:
                    print('Fail:' + IP)
                    with open(Fail_PATH, 'a+') as t:
                        t.write(IP + '\n')

else:
    IPS_PATH = 'IPS.txt'
    # 單個文件探測
    with open(IPS_PATH, 'r') as f:
        IPLIST = f.readlines()
        for IP in IPLIST:
            IP = IP.strip()
            URL = 'http://' + IP + '/cdn-cgi/trace'

            # 寫入當前探測的IP
            with open(Index_PATH, 'w') as i:
                i.write(IP)

            try:
                res = requests.get(URL, headers, timeout=timeout).text
            except:
                print('continue:' + IP)
                with open(Continue_PATH, 'a+') as t:
                    t.write(IP + '\n')
                continue

            if 'tls' in res:
                print('Success:' + IP)
                with open(Success_PATH, 'a+') as t:
                    t.write(IP + '\n')
            else:
                print('Fail:' + IP)
                with open(Fail_PATH, 'a+') as t:
                    t.write(IP + '\n')
