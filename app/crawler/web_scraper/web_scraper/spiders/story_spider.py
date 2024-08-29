import scrapy
from web_scraper.items import WebScraperItem

class StorySpider(scrapy.Spider):
    name = "story_spider"
    start_urls = ['https://example.com/trending']  # Replace with the actual URL

    def parse(self, response):
        for story in response.css('div.story'):
            item = WebScraperItem()
            item['title'] = story.css('h2::text').get()
            item['url'] = story.css('a::attr(href)').get()
            item['content'] = story.css('p::text').get()
            item['source'] = response.url
            yield item