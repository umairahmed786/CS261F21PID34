import pandas as pd
import time
from selenium import webdriver
from bs4 import BeautifulSoup
df=pd.read_csv('links.csv')
links=df.Links.values.tolist()
driver = webdriver.Chrome(executable_path='C:\\Users\\Umair Ahmed\\Downloads\\chromedriver_win32\\chromedriver.exe')

f = open("index.txt", "r")
index=int(f.read())



names=[]
addresses=[]
motos=[]
worldRanks=[]
countryRanks=[]
acronyms=[]
foundeds=[]
tels=[]
faxs=[]

count=1
for i in range(index,len(links)):
    driver.get("https://www.4icu.org/"+links[i])
    content = driver.page_source
    soup = BeautifulSoup(content)
    list1 = soup.findAll('div',attrs={'class':'row'})
    
#    name
    for a in list1:
        try:
            nam=a.find('h1', attrs={'itemprop':'name'})
            name = nam.text
        except:
            pass
    
    # table01
    # country rank
    # world_rank
    list2 = soup.find('table',attrs={'class':'text-right'})
    table1items = list2.findAll('strong')
    country_rank = table1items[0].text
    world_rank = table1items[1].text
    # print(country_rank, world_rank)
    
    
    
    list3 = soup.findAll('table',attrs={'class':'table borderless'})
    
    
    # acronym, founded, motto 
    list3trs = list3[0].findAll('tr')
    acronym = "None"
    founded = "None"
    motto = "None"
    for row in list3trs:
        if((row.find('th')).text == "Acronym"):
            acronym = row.find('strong').text
        if((row.find('th')).text == "Founded"):
            founded = row.find('strong').text
        if((row.find('th')).text == "Motto"):
            motto = row.find('strong').text
    # print(acronym, founded, motto)
    
    
    # address, tel, fax
    list3trs2 = list3[1].findAll('tr')
    address = ""
    tel = "None"
    fax = "None"
    for row in list3trs2:
        if((row.find('th')).text == "Address"):
            addressess = row.findAll('span')
            for i in addressess:
                address += " " + i.text
        if((row.find('th')).text == "Tel"):
            tel = row.find('span').text
        if((row.find('th')).text == "Fax"):
            fax = row.find('span').text
    names.append(name)
    addresses.append(address)
    worldRanks.append(world_rank)
    countryRanks.append(country_rank)
    acronyms.append(acronym)
    motos.append(motto)
    foundeds.append(founded)
    tels.append(tel)
    faxs.append(fax)
    count+=1
    index+=1
    time.sleep(1)
    if(count==11):
        df = pd.DataFrame({'Name':names, 'Acronyms':acronyms, 'Address':addresses,'Founded':foundeds,'Motto':motos,'WorldRank':worldRanks,'CountryRank':countryRanks,'Tel':tels,'Fax':faxs})
        df.to_csv('University.csv', mode='a' ,index=False, encoding='utf-8',header=False)
        f = open("index.txt", "w")
        f.write(str(index))
        f.close()
        count=1
        names=[]
        addresses=[]
        motos=[]
        worldRanks=[]
        countryRanks=[]
        acronyms=[]
        foundeds=[]
        tels=[]
        faxs=[]