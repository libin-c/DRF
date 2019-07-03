from . import views
from django.conf.urls import url, include

urlpatterns = [

    url(r'^books_serializer/$', views.BooksView.as_view()),
    url(r'^books_serializer/(?P<pk>\d+)/$', views.BookView.as_view()),
]
