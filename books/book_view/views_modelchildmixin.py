# Create your views here.

from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.


from book.models import BookInfo, HeroInfo
from book_serializer.serializers import BookMedolSerializer, BookSerializer


class BooksView(ListCreateAPIView):
    '''
    对所有图书整体操作
    '''
    #    指定视图使用的查寻集
    queryset = BookInfo.objects.all()
    #   指定视图使用的序列化器
    serializer_class = BookMedolSerializer




class BookView(RetrieveUpdateDestroyAPIView):
    '''
    单一图书操作
    '''
    #    指定视图使用的查寻集
    queryset = BookInfo.objects.all()
    #   指定视图使用的序列化器
    serializer_class = BookMedolSerializer

