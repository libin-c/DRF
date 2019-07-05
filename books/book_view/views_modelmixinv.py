# Create your views here.

from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
# Create your views here.


from book.models import BookInfo, HeroInfo
from book_serializer.serializers import BookMedolSerializer, BookSerializer


class BooksView(GenericAPIView, ListModelMixin, CreateModelMixin):
    '''
    对所有图书整体操作
    '''
    #    指定视图使用的查寻集
    queryset = BookInfo.objects.all()
    #   指定视图使用的序列化器
    serializer_class = BookMedolSerializer

    throttle_scope = 'contacts'

    # 01 显示所有图书
    def get(self, request):
        # 获得查询集所有数据
        return self.list(request)

    def post(self, request):
        return self.create(request)


class BookView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    '''
    单一图书操作
    '''
    #    指定视图使用的查寻集
    queryset = BookInfo.objects.all()
    #   指定视图使用的序列化器
    serializer_class = BookMedolSerializer

    throttle_scope = 'uploads'

    # 01 显示单一图书
    def get(self, request, pk):
        return self.retrieve(request, pk)

    # 02 更新图书
    def put(self, request, pk):
        # 1.0 取出数据

        return self.update(request, pk)

    # 03 删除图书
    def delete(self, request, pk):
        # 01 逻辑删除
        return self.destroy(request, pk)
