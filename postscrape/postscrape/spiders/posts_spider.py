import scrapy
from ..items import PostscrapeItem

class PostsSpider(scrapy.Spider):
    name = 'posts'
    start_urls = [
        'https://www.hongkiat.com/blog/pc-hardware-problems-solutions/'
    ]

    def parse(self, response):

        items = PostscrapeItem()

        page = response.css('div.container')

        for quote in page:
            problem = quote.css('h4::text').extract()
            solution = quote.css('p::text').extract()
            items['problem'] = problem
            items['solution'] = solution
            yield items