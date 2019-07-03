import json

from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import JsonResponse

from book.models import BookInfo, HeroInfo
from book_serializer.serializers import BookSerializer, HeroSerializer


class BooksView(View):
    '''
    对所有图书整体操作
    '''

    # 01 显示所有图书
    def get(self, request):
        books = BookInfo.objects.all()
        ser = BookSerializer(books, many=True)

        return JsonResponse(ser.data, safe=False)

    def post(self, request):
        # 1.0 获取数据
        books_date = request.body.decode()
        books_dict = json.loads(books_date)
        # 2.0 验证数据
        # btitle = books_dict.get('btitle')
        # if len(btitle) < 1:
        #     return JsonResponse({'error': '图书的名字不能为空'}, status=400)
        # 3.0 序列化器验证数据
        try:
            ser = BookSerializer(data=books_dict)
            ser.is_valid(raise_exception=True)
        except:
            return JsonResponse({'error': ser.errors})
        # if ser.errors is not None:
        #     return  JsonResponse({'error':ser.errors})
        # book_date = ser.validated_data
        # book = BookInfo.objects.create(**book_date)
        #  4.0 序列化器的保存
        ser.save()
        return JsonResponse(ser.data)


class BookView(View):
    '''
    单一图书操作
    '''

    # 01 显示单一图书
    def get(self, request, pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error': '查询的数据不存在'})
        ser = BookSerializer(book)
        # 1.0 复杂写法
        # heros = book.heroinfo_set.all()
        # hero_ser = HeroSerializer(heros, many=True)
        # # 构造英雄信息字典
        # hero_dict =hero_ser.data
        # date_dict = ser.data
        # date_dict['heros']=hero_dict
        # return JsonResponse(date_dict)

        return JsonResponse(ser.data)

    # 02 更新图书
    def put(self, request, pk):
        # 1.0 取出数据
        book_date = request.body.decode()
        book_dict = json.loads(book_date)
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error':"查询的图书不存在"})
        book.save()
        # 2.0 验证数据
        try:
            ser = BookSerializer(book, data=book_dict)
            ser.is_valid(raise_exception=True)
        except:
            return  JsonResponse({'error':ser.errors})
        # 03 更新数据
        # book = BookInfo.objects.get(id=pk)
        # book.btitle = book_dict.get('btitle')
        # # book.bpub_date = book_dict.get('bpub_date')
        # # book.bread = book_dict.get('bread')
        # # book.bcomment=book_dict.get('bcomment')
        # book.save()
        # BookInfo.objects.filter(id=pk).update(**book_dict)
        # book = BookInfo.objects.get(id=pk)
        # 04 返回数据
        ser.save()
        return JsonResponse(ser.data)

    # 03 删除图书
    def delete(self, request, pk):

        # 01 逻辑删除
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error': '查询的数据不存在'})
        book.is_delete = True
        book.save()
        # 02 物理删除
        # book = BookInfo.objects.filter(id=pk).delete()
        return JsonResponse({})
