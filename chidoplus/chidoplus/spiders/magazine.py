# -*- coding: utf-8 -*-
import scrapy
from chidoplus.items import ChidoplusItem

class MagazineSpider(scrapy.Spider):
    name = 'magazine'
    allowed_domains = ['chidoplus.com']

    magazines = ['hall', 'kitchen', 'bed-room',
                  'dinning', 'yard-and-trass', 'bath-room',
                  'paint', 'decor-2', 'layout',
                  'decor', 'living-room', 'wood-furniture',
                 'floor-covering', 'wall', 'other',
                 'enterance', 'baby-room', 'teens',
                 'small-apartment', 'nature', 'material']

    start_urls = ['https://chidoplus.com/magcat/{0}'.format(magazine) for magazine in magazines]

    custom_settings = {
        'DEPTH_LIMIT': '1',
    }

    def magcat (self, argument):
        switcher = {
            'https://chidoplus.com/magcat/hall/': 'نشیمن، هال و پذیرایی',
            'https://chidoplus.com/magcat/kitchen/': 'آشپزخانه',
            'https://chidoplus.com/magcat/bed-room/': 'اتاق خواب',
            'https://chidoplus.com/magcat/dinning/': 'نهار خوری',
            'https://chidoplus.com/magcat/yard-and-trass/': 'محوطه و تراس',
            'https://chidoplus.com/magcat/bath-room/': 'حمام و سرویس',
            'https://chidoplus.com/magcat/paint/': 'رنگ ها',
            'https://chidoplus.com/magcat/decor-2/': 'تزئینات',
            'https://chidoplus.com/magcat/layout/': 'چیدمان',
            'https://chidoplus.com/magcat/decor/': 'طراحی داخلی',
            'https://chidoplus.com/magcat/living-room/': 'خانه داری',
            'https://chidoplus.com/magcat/wood-furniture/': 'مبلمان و لوازم چوبی',
            'https://chidoplus.com/magcat/floor-covering/': 'بازسازی محل کار',
            'https://chidoplus.com/magcat/wall/': 'کفپوش و دیوارپوش',
            'https://chidoplus.com/magcat/other/': 'بازسازی و خرید خانه',
            'https://chidoplus.com/magcat/enterance/': 'ورودی خانه',
            'https://chidoplus.com/magcat/baby-room/': 'کودک',
            'https://chidoplus.com/magcat/teens/': 'نوجوان',
            'https://chidoplus.com/magcat/small-apartment/': 'آپارتمان های کوچک',
            'https://chidoplus.com/magcat/nature/': 'گل و گیاه',
            'https://chidoplus.com/magcat/material/': 'مصالح'
        }
        return switcher.get(argument,"Invalid Magazine Category")

    def parse(self, response):
        print(response.request.url)

        items = []

        magazine = self.magcat(response.request.url)
        articles = response.xpath('//*[@id="arve"]/body/div[3]/div[3]/div/article')
        for article in articles:
            item = ChidoplusItem()
            item['magazine'] = magazine
            item['title'] = article.xpath('div[2]/h2/a/@title').get()
            item['link'] = article.xpath('div[2]/h2/a/@href').get()
            item['summary'] = article.xpath('div[2]/p[2]/text()').get()
            items.append(item)
        print(items)
        return items
