# -*- coding: utf-8 -*-
import scrapy


class VerdiSpider(scrapy.Spider):
    name = 'verdi'
    allowed_domains = ['cines-verdi.com']
    start_urls = ['http://cines-verdi.com/']

    def parse(self, response):
        pass
