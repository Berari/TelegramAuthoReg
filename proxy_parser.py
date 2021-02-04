import  requests

from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class Parser:
    
    def __init__(self):
        
        self.html = requests.get('https://hidemy.name/ru/proxy-list/?type=hs#list', headers={'User-Agent': UserAgent().chrome})
        self.proxy_list = []

    def parser(self):

        soup = BeautifulSoup(self.html,'html.parser')

        blocks = soup.find('div', class_ = 'services_proxylist services').find('div', class_ = 'inner').find('div', class_ = 'table_block').find('table').find_all('tr')
        i = 0
        for block in blocks:
            if i == 0:
                i = i+1

            else:
                proxy = []
                data = block.find_all('td')
                ip = str(data[0]).split('<td>')[1].split('</td>')[0]
                port = str(data[1]).split('<td>')[1].split('</td>')[0]
                #print(ip)
                #print(port)

                proxy.append(ip)
                proxy.append(port)
                self.proxy_list.append(proxy)

        return self.proxy_list
