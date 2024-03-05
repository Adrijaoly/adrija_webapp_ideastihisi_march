import streamlit as sm
#from bs4 import BeautifulSoup
import os 
#import requests
#import csv
#import io
sm.title("Welcome to TIH information System!")
Result= sm.selectbox("Choose the location of TIH",("IIT Kharagpur","IIT Bombay","IIIT Hydrabad",
                                                         "IISc Bangalore","IIT Kanpur","IIT Jodhpur","IIT Roorkee",
                                                         "IIT Madras","IIT Hydrabad","IIT BHU","IIT Guwahati",
                                                         "IIT Mandi","IIT Delhi","IIT Ropar","IIT(ISM)Dhanbad","IIT Palakkad","IIIT Bangalore",
                                                         "IIT Indore","IIIT Delhi","IISER Pune","IIT Tirupati",
                                                         "IIT Bhilai","IIT Patna","ISI Kolkata"),index=None,placeholder="Choose from the options")

if Result=="IIT Kharagpur":
    with open("scraped_0_test.html", "r",encoding="utf-8") as f:
        html_data = f.read()
    sm.components.v1.html(html_data,height=1080,width=1980)
elif Result =="IIT Bombay":
    with open("scraped_1_test.html", "r",encoding="utf-8") as f:
        html_data = f.read()
    sm.components.v1.html(html_data,height=1580,width=1980)
elif Result == "IIIT Hydrabad":
   with open("scraped_2_test.html", "r",encoding="utf-8") as f:
        html_data = f.read()
   sm.components.v1.html(html_data,height=1980,width=1980)
elif Result == "IISc Bangalore":
    with open("scraped_3.html", "r",encoding="utf-8") as f:
        html_data = f.read()
    sm.components.v1.html(html_data,height=1980,width=1980)
elif Result =="IIT Kanpur":
    with open("scraped_4.html", "r",encoding="utf-8") as f:
        html_data = f.read()
    sm.components.v1.html(html_data,height=1980,width=1980)
elif Result == "IIT Jodhpur":
    with open("scraped_5.html", "r",encoding="utf-8") as f:
        html_data = f.read()
    sm.components.v1.html(html_data,height=1980,width=1980)
elif Result == "IIT Roorkee":
    with open("scraped_6.html", "r",encoding="utf-8") as f:
        html_data = f.read()
    sm.components.v1.html(html_data,height=2335,width=1980)
elif Result == "IIT Madras":
    with open("scraped_7.html","r",encoding="utf-8")as f:
        html_data=f.read()
    sm.components.v1.html(html_data,height=1980,width=1980)
elif Result == "IIT Hydrabad":
    with open("scraped_8.html","r",encoding="utf-8")as f:
        html_data=f.read()
    sm.components.v1.html(html_data,height=1980,width=1980)
elif Result == "IIT BHU":
    with open("scraped_9.html","r",encoding="utf-8")as f:
        html_data=f.read()
    sm.components.v1.html(html_data,height=1880,width=1980)
elif Result == "IIT Guwahati":
    with open("scraped_10.html","r",encoding="utf-8")as f:
        html_data=f.read()
    sm.components.v1.html(html_data,height=1980,width=1980)
elif Result == "IIT Ropar":
    with open("scraped_11_test.html","r",encoding="utf-8")as f:
        html_data=f.read()
    sm.components.v1.html(html_data,height=1980,width=1980)       
elif Result == "IIT Delhi":
    with open("scraped_12.html","r",encoding="utf-8")as f:
        html_data=f.read()
    sm.components.v1.html(html_data,height=2335,width=1980)
elif Result == "IIT Mandi":
    with open("scraped_13_test.html","r",encoding="utf-8")as f:
        html_data=f.read()
    sm.components.v1.html(html_data,height=1780,width=1980)
elif Result == "IIT(ISM)Dhanbad":
    with open("scraped_14.html","r",encoding="utf-8")as f:
        html_data=f.read()
    sm.components.v1.html(html_data,height=1980,width=1980)
elif Result == "IIT Palakkad":
    with open("scraped_15.html","r",encoding="utf-8")as f:
        html_data=f.read()
    sm.components.v1.html(html_data,height=1980,width=1980)
elif Result == "IIIT Bangalore":
    with open("scraped_16.html","r",encoding="utf-8")as f:
        html_data=f.read()
    sm.components.v1.html(html_data,height=1980,width=1980)
elif Result == "IIT Indore":
    with open("scraped_17.html","r",encoding="utf-8")as f:
        html_data=f.read()
    sm.components.v1.html(html_data,height=1980,width=1980)
elif Result == "IIIT Delhi":
    with open("scraped_18.html","r",encoding="utf-8")as f:
        html_data=f.read()
    sm.components.v1.html(html_data,height=1980,width=1980)
elif Result == "IISER Pune":
    with open("scraped_19.html","r",encoding="utf-8")as f:
        html_data=f.read()
    sm.components.v1.html(html_data,height=1980,width=1980)
elif Result == "IIT Tirupati":
    with open("scraped_20.html","r",encoding="utf-8")as f:
        html_data=f.read()
    sm.components.v1.html(html_data,height=1980,width=1980)
elif Result == "IIT Bhilai":
    with open("scraped_21.html","r",encoding="utf-8")as f:
        html_data=f.read()
    sm.components.v1.html(html_data,height=1980,width=1980)
elif Result == "IIT Patna":
    with open("scraped_22.html","r",encoding="utf-8")as f:
        html_data=f.read()
    sm.components.v1.html(html_data,height=1980,width=1980)
elif Result == "ISI Kolkata":
    with open("scraped_23.html","r",encoding="utf-8")as f:
        html_data=f.read()
    sm.components.v1.html(html_data,height=1980,width=1980)
else:
    sm.write("No options selected yet")

    

