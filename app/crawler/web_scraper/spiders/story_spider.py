import scrapy
from ..items import StoryItem
from datetime import datetime
from crawler.models import Article

class StorySpider(scrapy.Spider):
    name = "story_spider"
    start_urls = ['https://techcrunch.com']  # TechCrunch homepage

    def parse(self, response):
        for article in response.css('article.post-block'):
            title = article.css('h2.post-block__title a::text').get().strip()
            url = article.css('h2.post-block__title a::attr(href)').get().strip()
            summary = article.css('div.post-block__content::text').get().strip()
            publication_date = article.css('time::attr(datetime)').get().strip()
            publication_date = datetime.strptime(publication_date, '%Y-%m-%dT%H:%M:%S%z')

            # Save the scraped data to the database
            Article.objects.create(
                title=title,
                url=url,
                summary=summary,
                publication_date=publication_date,
                source='TechCrunch'
            )