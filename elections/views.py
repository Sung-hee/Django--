# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from requests import get
from bs4 import BeautifulSoup

import requests
# Create your views here.

def index(request):
    return HttpResponse("Hello world")

def naver(request):

    response = requests.get("https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=나혼자산다")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    for tqi in soup.select('input[name=tqi]'):
        print(tqi.get('value'))
        break
    
    response = requests.get("http://jsgetip.appspot.com/?getip")
    print(response.text.split('"')[1])
    response = requests.get("http://jsgetip.appspot.com/?getip", headers={'Host': response.text.split('"')[1]})
    return HttpResponse(response.text)