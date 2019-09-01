# -*- coding: utf-8 -*-
import scrapy
import json
import random


class KuaidiSpider(scrapy.Spider):
    name = 'kuaidi'
    allowed_domains = ['m.kuaidi100.com']
    start_urls=["https://m.kuaidi100.com/result.jsp?nu=71715525356997"]
    def start_requests(self):
        ma=random.random()
        print(ma)
        yield  scrapy.FormRequest("https://m.kuaidi100.com/query",callback=self.parse1,formdata={"postid":"75171522226157","type":"zhongtong","temp":str(ma),'valicode': '','id':'1',})
    def parse1(self, response):
        print(response.text+"+++++++++++++++++++++++++++++++++++++++++++++++++++")
        with open("1.txt","w") as f:
            f.write(response.text)
    def parse(self, response):
        print(response.text+"\n"+"\n")

