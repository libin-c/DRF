from . import views
from django.conf.urls import url, include
from . import views_genericapiviews

urlpatterns = [

    # url(r'^books_views/$', views.BooksView.as_view()),
    # url(r'^books_views/(?P<pk>\d+)/$', views.BookView.as_view()),

    url(r'^books_views/$', views_genericapiviews.BooksView.as_view()),
    url(r'^books_views/(?P<pk>\d+)/$', views_genericapiviews.BookView.as_view()),
]
