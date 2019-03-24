# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ChidoplusItem(Item):
    magazine = Field()
    title = Field()
    link = Field()
    summary = Field()
