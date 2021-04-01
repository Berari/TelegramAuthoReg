import  requests


from bs4 import BeautifulSoup

#from fake_useragent import UserAgent


class Parser:
    
    def __init__(self):
        
        self.html = requests.get('https://hidemy.name/ru/proxy-list/?type=s#list', headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.3.136 Yowser/2.5 Safari/537.36serpstatbot/2.0 beta (advanced backlink tracking bot; http://serpstatbot.com/; abuse@serpstatbot.com)'}).text
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

p = Parser()

proxy_list = p.parser()
for i in proxy_list:
    print(i)

#CheckProxy.main(proxyList = proxy_list)


