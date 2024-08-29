from rest_framework.generics import ListAPIView
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse

class ArticleListView(ListAPIView):
    """
    A view that returns all the articles in JSON format using Django REST Framework.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

def start_crawler(request):
    """
    A view that enqueues the web scraper to run as a background task.
    """
    from .tasks import enqueue_spider
    enqueue_spider()
    return JsonResponse({"message": "Web crawler task has been enqueued."})