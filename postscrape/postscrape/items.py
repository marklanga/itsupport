# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PostscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    problem = scrapy.Field()
    solution = scrapy.Field()

    pass
