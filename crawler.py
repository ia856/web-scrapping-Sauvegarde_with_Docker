from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen

url="https://www.sfds.asso.fr/fr/n/506-consulter_les_offres_demploi/?jedu=MASTER&jcon=&jp=3"
page=urlopen(url)
html=bs(page,'html.parser')
#print(html)
titre=html.find_all('td',{'class':'jobLabel'})

for element in titre :
    print (element.get_text())