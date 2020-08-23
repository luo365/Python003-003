# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SpidersPipeline:
    def process_item(self, item, spider):
        name = item['name']
        genre = item['genre']
        date_time = item['date_time']
        output = f'|{name}|; |{genre}|; |{date_time}|\n\n'
        with open('./mao_movies.csv', 'a+', encoding='utf-8') as article:
            article.write(output)
            
        return item
