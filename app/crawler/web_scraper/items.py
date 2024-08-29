import scrapy

class StoryItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
    source = scrapy.Field()