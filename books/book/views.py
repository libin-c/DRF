import json

from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import JsonResponse

from book.models import BookInfo


class BooksView(View):
    '''
    对所有图书整体操作
    '''

    # 01 显示所有图书
    def get(self, request):
        books = BookInfo.objects.all()
        book_info = []
        for book in books:
            book_info.append(
                {'id': book.id,
                 'btitle': book.btitle,
                 'bpub_date': book.bpub_date,
                 'bread': book.bread,
                 'bcomment': book.bcomment
                 }
            )
        return JsonResponse(book_info, safe=False)

    def post(self, request):
        books_date = request.body.decode()
        books_dict = json.loads(books_date)
        btitle = books_dict.get('btitle')
        if len(btitle) < 1:
            return JsonResponse({'error': '图书的名字不能为空'}, status=400)
        book = BookInfo.objects.create(**books_dict)
        content = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment
        }
        return JsonResponse(content)


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
        content = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment
        }
        return JsonResponse(content)

    # 02 更新图书
    def put(self, request, pk):
        # 1.0 取出数据
        book_date = request.body.decode()
        book_dict = json.loads(book_date)
        # 2.0 验证数据
        btitle = book_dict.get('btitle')

        if len(btitle) < 1:
            return JsonResponse({'error': '图书的名字不能为空'}, status=400)
        # 03 更新数据
        # book = BookInfo.objects.get(id=pk)
        # book.btitle = book_dict.get('btitle')
        # # book.bpub_date = book_dict.get('bpub_date')
        # # book.bread = book_dict.get('bread')
        # # book.bcomment=book_dict.get('bcomment')
        # book.save()
        BookInfo.objects.filter(id=pk).update(**book_dict)
        book = BookInfo.objects.get(id=pk)
        # 04 返回数据
        content = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment
        }
        return JsonResponse(content)

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
