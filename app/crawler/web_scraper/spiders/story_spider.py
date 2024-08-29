import scrapy
from ..items import StoryItem
from datetime import datetime
from crawler.models import Article

class StorySpider(scrapy.Spider):
    name = "story_spider"
    start_urls = ['https://news.google.com/topstories']  # Google News Top Stories

    def parse(self, response):
        # Scraping the headlines
        for article in response.css('article h3'):
            title = article.css('a::text').get()
            url = article.css('a::attr(href)').get()

            if title:
                title = title.strip()
            if url:
                # Google News URLs are relative, so they need to be joined with the base URL
                url = response.urljoin(url)

            # Log the scraped data for debugging
            self.logger.info(f"Scraped article: {title}, {url}")

            if title and url:
                try:
                    # Save the scraped data to the database
                    Article.objects.create(
                        title=title,
                        url=url,
                        summary='',  # Google News doesn't provide a summary in the headline
                        publication_date=datetime.now(),  # Set to now as Google News doesn't provide it
                        source='Google News'
                    )
                    self.logger.info(f"Saved article to database: {title}")
                except Exception as e:
                    self.logger.error(f"Error saving article: {e}")