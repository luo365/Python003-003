import scrapy
from scrapy import Selector
from douban_prj.items import DoubanPrjItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def start_requests(self):
        for i in range(8, 9):
            url = f'https://movie.douban.com/top250?start={i*25}&filter='
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        ms = Selector(response=response).xpath('//div[@class="info"]')
        for m in ms:
            title = m.xpath('./div[1]/a/span/text()').extract_first()
            director = m.xpath('./div[2]/p/text()').extract_first()
            director = director.split('主')[0].strip()
            director = director.split(':')[1].strip()
            rate = m.xpath('./div[2]/div/span[2]/text()').extract_first()
            item = DoubanPrjItem()
            item['title'] = title
            item['director'] = director
            item['rate'] = rate
            yield item
            


        
            
 