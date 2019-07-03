# Create your views here.

from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet
# Create your views here.


from book.models import BookInfo, HeroInfo
from book_serializer.serializers import BookMedolSerializer,BookSerializer


class BooksView(GenericViewSet):
    '''
    对所有图书整体操作
    '''
    #    指定视图使用的查寻集
    queryset = BookInfo.objects.all()
    #   指定视图使用的序列化器
    serializer_class = BookMedolSerializer

    # 01 显示所有图书
    def list(self, request):
        # 获得查询集所有数据
        books = self.get_queryset()
        ser = self.get_serializer(books, many=True)

        return Response(ser.data)

    def create(self, request):

        books_dict = request.data

        try:
            ser = self.get_serializer(data=books_dict)
            ser.is_valid(raise_exception=True)
        except:
            return Response({'error': ser.errors})

        ser.save()
        return Response(ser.data)


class BookView(GenericViewSet):
    '''
    单一图书操作
    '''
    #    指定视图使用的查寻集
    queryset = BookInfo.objects.all()
    #   指定视图使用的序列化器
    serializer_class = BookMedolSerializer

    # 01 显示单一图书
    def retrieve(self, request, pk):
        try:
            book = self.get_object()
        except:
            return Response({'error': '查询的数据不存在'})
        ser = self.get_serializer(book)

        return Response(ser.data)

    # 02 更新图书
    def update(self, request, pk):
        # 1.0 取出数据

        book_dict = request.data
        try:
            book = self.get_object()
        except:
            return Response({'error': "查询的图书不存在"})
        book.save()
        # 2.0 验证数据
        try:
            ser = self.get_serializer(book, data=book_dict)
            ser.is_valid(raise_exception=True)
        except:
            return Response({'error': ser.errors})
        # 03 更新数据

        # 04 返回数据
        ser.save()
        return Response(ser.data)

    # 03 删除图书
    def destroy(self, request, pk):

        # 01 逻辑删除
        try:
            book = self.get_object()
        except:
            return Response({'error': '查询的数据不存在'})
        book.is_delete = True
        book.save()

        return Response({})
