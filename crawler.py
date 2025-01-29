from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
import pandas as pd

url="https://www.sfds.asso.fr/fr/n/506-consulter_les_offres_demploi/?jedu=MASTER&jcon=&jp=3"
page=urlopen(url)
html=bs(page,'html.parser')
#print(html)
titre=html.find_all('td',{'class':'jobLabel'})

##for element in titre :
    ##print (element.get_text())


allJobs = html.find_all('div', class_='job') 
titre_offre=[]
date_offre=[]
resume_offre=[]

for job in allJobs:
    for titles in job.find_all('td',{'class':'jobLabel'}):
        title=titles.get_text()
        titre_offre.append(title)

    datepubs = job.find_all('td',{'class':'jobPublished'})
    date=datepubs[0].get_text()
    date_offre.append(date)

    for resumes in job.find_all('td',{'class':'jobResume'}):
        resume=resumes.get_text()
        resume_offre.append(resume)

    
# Print all Titles Jobs
#print(titre_offre)

# Print all Date Pub
#print(date_offre)

# Print all Resume
#print(resume_offre)


dfJobs=pd.DataFrame({
    'TITRE_OFFRE':titre_offre,
    'DATE_OFFRE':date_offre,
    'RESUME_OFFRE':resume_offre
})
#dfJobs.to_csv('jobs.csv')

# create sqlalchemy engine
user='root'
passw='supersecret'
host='localhost' # either localhost or ip e.g? '172.17.0.2' or hostname adress
port=3307
database='jobs_scraping'

engine=create_engine('mysql+pymysql://' + user + ':' + passw + '@' + host + ':' + str(port) + '/' + database , echo=False)
dfJobs.to_sql('jobs' , con=engine, if_exists = 'append' , index = False, chunksize = 1000)