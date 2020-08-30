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
        movies = []
        # title_txts = []
        # titles = Selector(response=response).xpath('//*[@id="content"]/div/div[1]/ol/li/div/div/div[1]/a')
        # for title in titles:
        #     title_txt = title.xpath('./span/text()').extract_first()
        #     title_txts.append(title_txt)


        # director_txts = []
        # directors = Selector(response=response).xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[1]')
        # for director in directors:
        #     director_txt = director.xpath('./text()').extract_first().strip()
        #     director_txt = director_txt.split('主')[0].strip()
        #     director_txt = director_txt.split(':')[1].strip()
        #     director_txts.append(director_txt)


        # rate_txts = []
        # rates = Selector(response=response).xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[2]')
        # for rate in rates:
        #     rate_txt = rate.xpath('./text()').extract_first().strip()
        #     rate_txts.append(rate_txt)

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
            


        
            
 