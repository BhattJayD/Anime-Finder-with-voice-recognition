from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import speech_recognition as sr
import os

anime=input("Enter Anime NAME:- ")

driver=webdriver.Chrome()
driver.get('https://4anime.to/')



time.sleep(25)
input("press anything after capcha")
searchbox=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/header/div[3]/div/ul[3]/div[1]/div/div[2]/form/input[1]')
searchbox.send_keys(anime)
time.sleep(3)
searchbtn=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/header/div[3]/div/ul[3]/div[1]/div/i[1]')
searchbtn.click()
time.sleep(10)
aa=driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[1]/div/a')
aa.click()
time.sleep(2)
ep=driver.find_element_by_xpath('/html/body/div[1]/div/div/section/div[1]/div/div/div[2]/div[4]/div[1]/section/div/div/div/div/ul/li[1]/a')
ep.click()
time.sleep(2)
plybtn=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/section/div/div[2]/center/div/div[7]/div[1]/div')
plybtn.click()