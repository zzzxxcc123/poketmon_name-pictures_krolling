##필수 
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os 

## 선택
from time import sleep

#오류없이 파일 만들기 알고리즘 
##퍼일 있으면 PASS
def makefile(x):
    if os.path.isdir(x):
        pass
    else:
        os.mkdir(x)
        
##이름 오류없이 만들기
def dele(x):
    for i in ":/<\\\">|?*":
        x=x.replace(i,"")
    return x

## 창 숨기기 모드
options=webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("window-size=1920x1080")
options.add_argument("disable-gpu")

driver = webdriver.Chrome("chromedriver.exe",chrome_options=options)

## URL선택
driver.get("https://pokemongo.inven.co.kr/dataninfo/pokemon/")
hp = driver.page_source
sleep(2)
soup = BeautifulSoup(hp,"html.parser")

## class - .  id - 없음 
for i in soup.select(".pokemonicon"):
    name = dele(i.select_one(".pokemonname").text)

    ##그림 가져오기
    url = "https:" + i.select_one("img").get("src")
    r = requests.get(url)
    
    f=open(f"poke/{name}.png" , "wb")
    f.write(r.content)



