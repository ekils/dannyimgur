#coding=utf-8

import re
from bs4 import BeautifulSoup
import requests
import urllib.request
import os
import sys
import time
import urllib
from selenium import webdriver


class imgur:
    def __init__(self):
        service_args = []
        service_args.append('--load-images=no')  # 關閉圖片加載
        service_args.append('--disk-cache=yes')  # 開啟緩存
        service_args.append('--ignore-ssl-errors=true')  # 忽略https錯誤
        self.driver = webdriver.PhantomJS(executable_path='/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs', service_args=service_args)

    def statistics(self):
        url= input('Paste imgur url: ')
        hash = re.compile('hash\":\"[a-zA-Z0-9]{0,10}')
        try:
            page =(url).  # example: https://imgur.com/a/J9ZWQ
            driver =self.driver
            driver.get(page)
            soups = BeautifulSoup(driver.page_source, "html.parser")
            # print(type(soups))
            hash_key = hash.findall(str(soups))
            hash_key_url = ['http://i.imgur.com/'+ i.split('hash":"')[1]+'.jpg' for i in hash_key]

            print(hash_key_url)

            oripath= os.getcwd()

            count = len(hash_key_url)

            if not os.path.exists(oripath + '/'+'photos'):
                os.mkdir(oripath+'/'+'photos')
            os.chdir(oripath+'/'+'photos')

            print('\n')
            for i,ii in enumerate(hash_key_url):
                url_photo = urllib.request.urlopen(ii).read()
                with open(hash_key[i].split('hash":"')[1]+".jpg",'wb') as f:
                    f.write(url_photo)
                    sys.stdout.write('\r')
                    sys.stdout.write('{} photos left'.format(count))
                    count = count -1
                    f.close()
                    sys.stdout.flush()
            os.chdir(oripath)
        except:
            print('except')



igr= imgur()
igr.statistics()
