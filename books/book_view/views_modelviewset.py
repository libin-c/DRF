from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.viewsets import ModelViewSet
# 排序方法
from rest_framework.filters import OrderingFilter
#   分页方法
from rest_framework.pagination import PageNumberPagination

from django.db import DatabaseError
from book.models import BookInfo, HeroInfo
from book_serializer.serializers import BookMedolSerializer, HeroSerializer


# 自定义分页器
class PageNumber(PageNumberPagination):

    # 如果前段没传pagesize 就按照这个page_size 参数的个数来传


    page_size = 5
    # 指定页的参数
    page_query_param = 'page'
    # 指定分页的个数参数
    page_size_query_param = 'page_size'

    # 返回前段的最大个数
    max_page_size = 100


#
# class BookModelViewSet(ModelViewSet):
#     #    指定视图使用的查寻集
#     queryset = BookInfo.objects.all()
#     #   指定视图使用的序列化器
#     serializer_class = BookMedolSerializer
#
#     def last(self, request):
#         hero = HeroInfo.objects.latest('id')
#         ser = HeroSerializer(hero)
#         return Response(ser.data)
#
#     def hero(self, request):
#         hero = HeroInfo.objects.all()
#         ser = HeroSerializer(hero, many=True)
#         return Response(ser.data)

class BookModelViewSet(ModelViewSet):
    """
     get:
     返回所有图书信息.

     post:
     新建图书.

      list:
     返回图书列表数据

     retrieve:
     返回图书详情数据

     latest:
     返回最新的图书数据

     read:
     修改图书的阅读量
     """

    #    指定视图使用的查寻集
    queryset = BookInfo.objects.all()
    #   指定视图使用的序列化器
    serializer_class = BookMedolSerializer
    # 添加过滤字段
    # filter_fields = ('btitle', 'bread')
    # filter_backends = [OrderingFilter]
    # ordering_fields = ('id', 'bread', 'bpub_date')

    pagination_class = PageNumber

    # 权限
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # #   认证
    # permission_classes = (IsAuthenticated,)
    # #   限流
    # throttle_classes = (UserRateThrottle,)

    def get_serializer_class(self):
        if self.action == 'hero':
            return HeroSerializer
        else:
            return BookMedolSerializer

    @action(methods=['get'], detail=False)
    def last(self, request):
        raise DatabaseError
        book = BookInfo.objects.latest('id')
        ser = self.get_serializer(book)
        return Response(ser.data)

    @action(methods=['get'], detail=False)
    def hero(self, request):
        hero = HeroInfo.objects.all()
        ser = self.get_serializer(hero, many=True)
        return Response(ser.data)
