from selenium import webdriver
from urllib.request import urlretrieve
import time
import os
SLEEP_TIME = 2

try:
    driver = webdriver.Chrome('.\chromedriver.exe')
except:
    print("you need chromedriver in the same folder")

# 웹자원 로드를 위해 기다림
driver.implicitly_wait(SLEEP_TIME)

while(True):
    gifType = input("Do you want Sticker or Gif? (s/g)")
    if(gifType == "s"):
        driver.get('https://tenor.com/official/southpark/stickers')
        dirPath = ".\southpark's Stickers"
        break
    elif (gifType =="g"):
        driver.get('https://tenor.com/official/southpark')
        dirPath = ".\southpark's GIFs"
        break
        
driver.implicitly_wait(SLEEP_TIME)


if not os.path.isdir(dirPath):
    os.mkdir(dirPath)


def downloadImg():
    time.sleep(SLEEP_TIME)
    fileName = driver.find_element_by_css_selector("#view > div > div > h1").text
    print(fileName)

    img = driver.find_element_by_css_selector("div.Gif > img")
    imgLink = img.get_attribute('src')
    start = imgLink.rfind('.')
    end = imgLink.rfind('?')
    if end==-1:
        filetype = imgLink[start:]
    else: 
        filetype = imgLink[start:end]
    try:
        if fileName=="":
            fileName = "no_name"
        if os.path.isfile(dirPath+f"\{fileName}{filetype}"):
            fileName = fileName+"(2)"
        urlretrieve(imgLink, dirPath+f"\{fileName}{filetype}")
        print(f"{fileName}{filetype} Downloded")
    except:
        print(f"{fileName}{filetype} Download fail")
        pass
    driver.back()
    time.sleep(SLEEP_TIME)

errorcount = 0

count = 0
last_height = driver.execute_script("return document.body.scrollHeight")
while True: 
    
    time.sleep(SLEEP_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")

    try:
        while True:
            try:
                time.sleep(SLEEP_TIME)
                image = driver.find_element_by_xpath(f"//figure[@data-index='{count}']/a")
                image.click()
                downloadImg()
                count +=1
            except:
                driver.execute_script("window.scrollTo(0, (window.scrollY+100));")
                last_height = new_height
                new_height = driver.execute_script("return document.body.scrollHeight")
                errorcount +=1
                if(last_height == new_height) or errorcount >20:
                    break
                pass


    except:
        print("error")
        errorcount += 1
        pass

    last_height = new_height

    if errorcount >20:
        print(f"count : {count}")

        break

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        print("same height")

        print(f"count : {count}")

        break
    

driver.close()
