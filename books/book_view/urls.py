from . import views, views_genericapiviews, views_modelmixinv, views_modelchildmixin, views_viewset, \
    views_genericviewset, views_modelviewset
from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter,DefaultRouter

urlpatterns = [

    # url(r'^books_views/$', views.BooksView.as_view()),
    # url(r'^books_views/(?P<pk>\d+)/$', views.BookView.as_view()),

    # url(r'^books_views/$', views_genericapiviews.BooksView.as_view()),
    # url(r'^books_views/(?P<pk>\d+)/$', views_genericapiviews.BookView.as_view()),

    # url(r'^books_views/$', views_modelmixinv.BooksView.as_view()),
    # url(r'^books_views/(?P<pk>\d+)/$', views_modelmixinv.BookView.as_view()),

    # url(r'^books_views/$', views_modelchildmixin.BooksView.as_view()),
    # url(r'^books_views/(?P<pk>\d+)/$', views_modelchildmixin.BookView.as_view()),

    # url(r'^books_views/$', views_viewset.BooksView.as_view({'get':'list','post':'create'})),
    # url(r'^books_views/(?P<pk>\d+)/$', views_viewset.BookView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    #
    # url(r'^books_views/$', views_modelviewset.BookModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    # url(r'^books_views/(?P<pk>\d+)/$',
    #     views_modelviewset.BookModelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    # url(r'^books_views/last/$', views_modelviewset.BookModelViewSet.as_view({'get': 'last'})),
    # url(r'^books_views/hero/$', views_modelviewset.BookModelViewSet.as_view({'get': 'hero'})),

]
router = SimpleRouter()
router.register('books_views', views_modelviewset.BookModelViewSet, base_name='books_views')
print(router.urls)
urlpatterns += router.urls
