from django.urls import path
from .views import start_crawler, ArticleListView

urlpatterns = [
    path('start-crawler/', start_crawler, name='start-crawler'),
    path('articles/', ArticleListView.as_view(), name='article-list'),

]