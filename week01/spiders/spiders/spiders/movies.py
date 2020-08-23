import scrapy
from spiders.items import MaoyanItem
from scrapy.selector import Selector


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = []

        movies = Selector(response=response).xpath('//div[contains(@class, "channel-detail")]')
        for movie in movies:
            name = movie.xpath('./a/text()')
            url = movie.xpath('./a/@href')
            if len(name) > 0:
                name = name.extract_first().strip()
                url = url.extract_first().strip()

                url = 'https://maoyan.com' + url
                item = MaoyanItem()
                item['name'] = name
                item['url'] = url
                items.append(item)
                yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse_page)

            if len(items) == 10:
                break

    def parse_page(self, response):
            item = response.meta['item']
            genres = Selector(response=response).xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li')
            genre_txt = ''
            for genre in genres:
                genre_txt += genre.xpath('./a/text()')
                genre_txt += ','
            item['genre'] = genre_txt        

            yield item