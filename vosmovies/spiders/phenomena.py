# -*- coding: utf-8 -*-
import scrapy
import datetime
import re


class PhenomenaSpider(scrapy.Spider):
    name = 'phenomena'
    def __init__(self):
        scrapy.Spider.__init__(self)
        self.current_date = datetime.datetime.now().strftime("%m-%Y")

    def start_requests(self):
        allowed_domains = ['http://www.phenomena-experience.com']
        start_urls = [f'http://www.phenomena-experience.com/programacion-mensual/{self.current_date}.html']
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def extract(self, movie):
        title = movie.xpath(".//div[contains(@class, 'event-titulo')]/a/text()").get().strip()
        details = re.sub("\n|\t|·|&middot|\s{2}", "", movie.xpath(".//div[contains(@class, 'event-datos')]/text()").get()).strip()
        return {
                "title" : title,
                "details" : details,
                }


    def parse(self, response):
        day = response.xpath("//*[contains(@class, 'clasemensual')]")[0]
        movies = day.xpath("//*[contains(@class, 'event-content')]")
        print (list(map(self.extract, movies)))
        return list(map(self.extract, movies))

        



    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = 'quotes-%s.html' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Saved file %s' % filename)
