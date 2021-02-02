import  requests
import lxml

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from fp.fp import FreeProxy

def test():
    proxies = {
        'http': '182.53.50.184:8081',
        #'https': '35.156.9.227:8080'
    }

    response = requests.get(url = 'https://2ip.ru/', proxies=proxies)

    print(response)

    proxy = FreeProxy(country_id=['RU', 'BR'], timeout=0.3, rand=True).get()
    print(proxy)

    re = requests.get(url = 'https://2ip.ru/', proxies=proxies)

    print(re)

class Parser:
    
    def __init__(self, html):
        
        self.html = html

    def parser(self):

        soup = BeautifulSoup(self.html,'html.parser')

        blocks = soup.find('div', class_ = 'services_proxylist services').find('div', class_ = 'inner').find('div', class_ = 'table_block').find('table').find_all('tr')
        i = 0
        for block in blocks:
            if i == 0:
                i = i+1

            else:
                data = block.find_all('td')
                ip = str(data[0]).split('<td>')[1].split('</td>')[0]
                port = str(data[1]).split('<td>')[1].split('</td>')[0]
                print(ip)
                print(port)




def main():
    response = requests.get('https://hidemy.name/ru/proxy-list/?type=hs#list', headers={'User-Agent': UserAgent().chrome})

    p = Parser(html = response.text)
    p.parser()
    test()
    
if __name__ == '__main__':
    main()


    