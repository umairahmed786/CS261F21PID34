from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome(executable_path='C:\\Users\\Umair Ahmed\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get("https://www.4icu.org/reviews/index0001.htm")
content = driver.page_source
soup = BeautifulSoup(content)
alphabets=[]
for a in range(2,28):
    alphabets.append("https://www.4icu.org/reviews/index"+str(a)+".htm")
    import time
import pandas as pd
for i in range(2,len(alphabets)):
    universities=[]
    driver.get(alphabets[i])
    content = driver.page_source
    soup = BeautifulSoup(content)
    list1 = soup.findAll('a', href=True)
    for a in list1:
        uni=a['href']
        if '/reviews/' in uni:
            universities.append(uni)
    universities.pop(0)
    universities.pop(0)
    universities.pop(len(universities)-1)
    df = pd.DataFrame({'Links':universities})
    #df.to_csv('links.csv', index=False, encoding='utf-8')
    df.to_csv('links.csv', mode='a', index=False, header=False)
    time.sleep(5)
    
        
    