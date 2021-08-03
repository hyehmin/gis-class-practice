from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import ArticleCreateView

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html')),

    path('create/', ArticleCreateView.as_view(), name='create'),
]