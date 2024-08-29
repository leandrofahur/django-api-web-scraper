from django.http import HttpResponse
from tasks import enqueue_spider

def start_crawler(request):
    """
    This view triggers the background task to run the Scrapy spider.
    """
    enqueue_spider()
    return HttpResponse("Web crawler task has been enqueued!")