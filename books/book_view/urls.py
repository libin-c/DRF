from . import views
from django.conf.urls import url, include
from . import views_genericapiviews
from . import views_modelmixinv
from . import views_modelchildmixin

urlpatterns = [

    # url(r'^books_views/$', views.BooksView.as_view()),
    # url(r'^books_views/(?P<pk>\d+)/$', views.BookView.as_view()),

    # url(r'^books_views/$', views_genericapiviews.BooksView.as_view()),
    # url(r'^books_views/(?P<pk>\d+)/$', views_genericapiviews.BookView.as_view()),

    # url(r'^books_views/$', views_modelmixinv.BooksView.as_view()),
    # url(r'^books_views/(?P<pk>\d+)/$', views_modelmixinv.BookView.as_view()),

    url(r'^books_views/$', views_modelchildmixin.BooksView.as_view()),
    url(r'^books_views/(?P<pk>\d+)/$', views_modelchildmixin.BookView.as_view()),
]
