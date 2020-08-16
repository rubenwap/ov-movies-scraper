# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VosmoviesItem(scrapy.Item):
    cinema = scrapy.Field()
    date = scrapy.Field()
    details = scrapy.Field()
    hour = scrapy.Field()
    title = scrapy.Field()
    timestamp = scrapy.Field()

