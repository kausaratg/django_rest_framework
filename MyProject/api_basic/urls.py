from django.urls import path
from api_basic.views import article_list, article_detail

urlpatterns = [
    path('api/', article_list, name="article_list"),
    path("detail/<int:pk>", article_detail, name="article_detail")
]
