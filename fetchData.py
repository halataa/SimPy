import requests
import re
import csv
from bs4 import BeautifulSoup as BS

startPage = 1
endPage = 500 # 500 recomended


NPDict = dict()

with open('NPfile.csv', 'r') as NPfile:
    csvReader = csv.reader(NPfile)
    for line in csvReader:
        if line != []:
            NPDict[line[0]] = line[1]

for i in range(startPage, endPage+1):
    NPList = list()
    Nlist = list()
    Plist = list()
    r = requests.get('https://www.rond.ir/SearchSim/Mci/912?page=%s&StateId=0&CityId=0&SimOrderBy=Update&ItemPerPage=120' % (i))
    print('Page : %s' % i)
    soup = BS(r.text, 'html.parser')
    Ns = soup.findAll('a', attrs={'class': 't-link'})
    Ps = soup.findAll('td')
    for N in Ns:
        Nlist.append(N.text.strip())
    for P in Ps:
        try:
            Plist.append(P.span.text)
        except:
            pass
    print('Items on page : %s' % (len(Ns)))
    for j in range(len(Ns)):
        a = re.sub(r'\D', '', Nlist[j])
        b = re.sub(r'\D', '', Plist[j])
        if a and b != '':
            if a.startswith('0') == False:
                a = '0' + a
            NPList.append([a, b])

    with open('NPfile.csv', 'a') as NPfile:
        writer = csv.writer(NPfile)
        k = 0
        for NP in NPList:
            if NP[0] not in NPDict:
                NPDict[NP[0]] = NP[1]
                writer.writerow(NP)
                k += 1
        print('New Item : %s' % (k))
    print('New Total : %s' % (len(NPDict.values())))
    print('----------------------')
