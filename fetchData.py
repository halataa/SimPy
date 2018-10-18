import requests
import re
from bs4 import BeautifulSoup as BS
numberOfPages = 2
NPList = list()
Nlist = list()
Plist = list()
for i in range (1,numberOfPages):
    r = requests.get('https://www.rond.ir/SearchSim/Mci/912?page=%s&StateId=0&CityId=0&SimOrderBy=Update&ItemPerPage=120'%(i))
    soup = BS(r.text,'html.parser')
    Ns = soup.findAll('a',attrs={'class':'t-link'})
    Ps = soup.findAll('td')
    for N in Ns:
        Nlist.append(N.text.strip())
    for P in Ps:
        try:
            Plist.append(P.span.text)
        except:
            pass
    for j in range(len(Ns)):
        a = re.sub(r'\D','',Nlist[j])
        b = re.sub(r'\D','',Plist[j])
        if a and b != '' and a.startswith('0') == True:
            NPList.append([a,b])
    for np in NPList:
        print(np)