from . import views
from django.conf.urls import url, include

urlpatterns = [

    url(r'^books/$', views.BooksView.as_view()),
    url(r'^books/(?P<pk>\d+)/$', views.BookView.as_view()),
]
