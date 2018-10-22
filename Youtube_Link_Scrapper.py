# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 12:16:11 2018

@author: Karim Noor Ali
"""

from selenium import webdriver

chrome_path = r"F:\chromedriver.exe" #Download Chrome driver and specify the path
driver = webdriver.Chrome(chrome_path)

num = input("How many links you want to extract max?") #Specify the number of links you want to scrape
query = input("Your search query?") #Enter the keyword you want to search. Make sure if there is a space -
                                    #- in your keyword, replace it with a '+' For Eg: MO Vlogs will be MO+Vlogs

url = 'https://www.youtube.com/results?search_query='+ query

driver.get(url)

Collect_links = []
links = []
link_num = 0

x = '0'
y = '1000'

#loop to extract the video links from the Page
while link_num < int(num):
    elems = driver.find_elements_by_xpath("//a[@href]") #Scraping all the links
    for elem in elems:
        Collect_links.append(elem.get_attribute("href"))
    for w in Collect_links:
        if w.startswith('https://www.youtube.com/watch?') and w not in links: #Filtering links
            links.append(w)
            print(w)
            link_num = link_num + 1
        if link_num == num:
            break   
    driver.execute_script("window.scrollTo( %s , %s )"%(x,y)) #Scrolling to collect the target number of links
    x = y
    y = str(int(x) + 1000)  