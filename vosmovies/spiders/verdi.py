# -*- coding: utf-8 -*-
import scrapy
import locale
import datetime


class VerdiSpider(scrapy.Spider):
    name = 'verdi'
    locale.setlocale(locale.LC_ALL, 'es_ES')
    
    def start_requests(self):
        allowed_domains = ['http://www.cines-verdi.com/']
        start_urls = ['http://www.cines-verdi.com/barcelona/cartelera/']
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def extract(self, movie):
        today_is = datetime.datetime.today().strftime("%A %d de %B de %Y")
        day = movie.xpath(".//following-sibling::table/tr[1]/th/text()").get().strip()
        hours = movie.xpath(".//following-sibling::table/tr[1]/td/a/text()").getall()

        if day.lower() == today_is.lower():
            title = movie.xpath(".//tr/td/@id").get()
            return {
                    "title" : title.strip(),
                    "details" : "No details available",
                    "hour" : hours,
                    "date": day.strip(),
                    "cinema" : "Verdi"
                    }

    def parse(self, response):
        movies = response.xpath("//*[contains(@class, 'carteleraTitulo')]")
        return list(map(self.extract, movies))

