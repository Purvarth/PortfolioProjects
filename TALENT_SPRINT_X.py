# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 22:01:14 2021

@author: Purvarth
"""



from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
#import re

#variables
course_name = []
course_link = []
course_desc = []
course_duration = []
course_inst = []
course_prof = []
course_prof1 = []
course_prof2 = []
course_certificate = []
course_price = []
n = 0
link = "https://talentsprint.com/programs.dpl#technologies"


#webdriver
driver = webdriver.Chrome('C:\Program Files (x86)/chromedriver')


#BeautifulSoup
r = requests.get(link)
soup = BeautifulSoup(r.content, "html5lib")

#course name
name = soup.find_all(class_='program_blocks')

#Data scraping loop
for i in name:
    course_link.append(i.div.a["href"].strip())
    course_name.append(i.div.h3.text.strip())
    #course_desc.append(i.div.ul.text.strip())
    
    try:
        course_duration.append(i.div.findAll('p')[1].text.replace("Know More" , "-").strip())
    except:
        course_duration.append("-")
    
    try:
        course_inst.append(i.div.h2.text.replace("Program Partner" , "").strip())
    except:
        course_inst.append('-')    
    #print(k+1,course_name[k])
    '''
    k = requests.get(course_link[n])
    soup1 = BeautifulSoup(k.content , "html5lib")
    
    try:
        name = soup1.find_all('table' , class_='pricing-tab')
        for names in name:
            course_price.append(names.findAll('td')[1].text.strip())
    except:
        course_price.append("-")
    
    n = n + 1
    '''

'''
for i in range(len(course_name)):
    r = requests.get(course_link[i])
    soup = BeautifulSoup(r.content, "html5lib")
    nameSUB = soup.find_all(class_="col-md-8")
   
    for k in nameSUB:
        try:
            course_desc.append(k.div.text.strip())
        except:
            course_desc.append("-")
'''

#parent cell
for n in range(len(course_name)):
    r = requests.get(course_link[n])
    soup = BeautifulSoup(r.content , "html5lib")
    
    #course desc
    try:
        name = soup.find('div' , attrs = {"class" : "aboutProgram"})
        course_desc.append(name.p.text.strip())
    except:
        
        try:
           name = soup.find('div' , attrs = {"id" : "aboutProgram"})
           course_desc.append(name.p.text.strip()) 
        except:
           
            try:
                name = soup.find('div' , attrs = {"class" : "about"})
                course_desc.append(name.p.text.strip()) 
            except:
             
                try:
                    name = soup.find('div' , attrs = {"id" : "about"})
                    course_desc.append(name.p.text.strip())
                except:
                
                    try:
                       name = soup.find('div' , attrs = {"class" : "aboutprogram"})
                       course_desc.append(name.p.text.strip())
                    except:
                       course_desc.append("-")
    
    #pricing
    try:
        name = soup.find('table' , class_='pricing-tab')
        course_price.append(name.findAll('td')[1].text.replace('₹' , '').strip().split()[-1])
    except:
        course_price.append("-")

    #course prof
    try:
        name = soup.find('div' , attrs = {'id' : 'faculty'})
        try:
            course_prof1.append(name.h4.text.replace('Program','').replace('Prof.', '').replace('Dr.','').strip().split()[0])
        except:
            course_prof1.append("-")
        try:
            course_prof2.append(name.h4.text.replace('Program','').replace('Prof.', '').replace('Dr.','').strip().split()[1])
        except:
            try:                    
                driver.get(course_link[i])
                time.sleep(5)
                driver.execute_script("window.scrollTo(0, 3800)")
                time.sleep(5)
                driver.find_element_by_xpath('//*[@id="accordion1"]/div[2]/div[1]/h4/a').click()
                time.sleep(5)
                name = driver.find_element_by_xpath('//*[@id="leadFaculty"]/div/ul/li[1]').find_element_by_tag_name("h4")
                course_prof.append(name.text)
                time.sleep(5)
            except:
                course_prof2.append('-')
   
    except:
        course_prof.append("-")

#course prof
'''
for i in range(len(course_name)):
    time.sleep(10)
    driver.get(course_link[i])
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, 3800)")
    time.sleep(5)
    try:
        driver.find_element_by_xpath('//*[@id="accordion1"]/div[2]/div[1]/h4/a').click()
        time.sleep(5)
    except:
        try:
            r = requests.get(course_link[i])
            soup = BeautifulSoup(r.content , "html5lib")
            name = soup.find('div' , attrs = {"class" : "aboutProgram"})
            course_desc.append(name.p.text.strip())
        except:
            
driver.quit()
'''



'''              
#course desc
for n in range(len(course_link)):
    r = requests.get(course_link[0])
    soup = BeautifulSoup(r.content , "html5lib")
    
    try:
        name = soup.findAll('div' , attrs = {"class" : "aboutProgram"})
        course_desc.append(name.p.text.strip())
    except:
        name = soup.findAll('div' , attrs = {"id" : "aboutProgram"})
        course_desc.append(name.p.text.strip())  
'''    


'''
#pricing
for i in range(len(course_name)):
    k = requests.get(course_link[i])
    soup1 = BeautifulSoup(k.content , "html5lib")
    
    try:
        name = soup1.find('table' , class_='pricing-tab')
        course_price.append(name.findAll('td')[1].text.replace('₹' , '').strip().split()[-1])
    except:
        course_price.append("-")
''' 
     
#testing    
for i in range(len(course_name)): 
    print(i+1,">",course_name[i]) 
    time.sleep(0.3)
    #print(course_link[i])
    #time.sleep(0.3)
    #print(course_duration[i])
    #time.sleep(0.3)
    #print(course_inst[i])
    #time.sleep(0.3)
    print(course_desc[i], '\n')
    #time.sleep(0.3)
    course_prof[i] = course_prof1[i] +' '+ course_prof2[i]
    if (course_prof[i] == '- -'):
        course_prof[i] = '-'
    print(course_prof[i], '\n')
    print(course_price[i], '\n')
    i = i + 1
    time.sleep(1)
   
#driver exit
driver.quit()


#Excel  
course_summary = pd.DataFrame()

course_summary["course_name"] = course_name
course_summary["course_inst"] = course_inst
course_summary["course_desc"] = course_desc
course_summary["course_prof"] = course_prof
course_summary["course_price"] = course_price
course_summary["course_duration"] = course_duration
course_summary["course_link"] = course_link

course_summary.to_csv("Talent_Sprint.csv", encoding = "utf-8")
  