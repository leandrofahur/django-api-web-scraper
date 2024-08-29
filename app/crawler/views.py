from django.http import HttpResponse
from .tasks import enqueue_spider

def start_crawler(request):
    enqueue_spider()
    return HttpResponse("Web crawler task has been enqueued!")