# views 视图函数
from DRF_demo.serializers import BookSerializer


class BooksViews(object):
    def post(self, data):
        # 1 接收参数
        data = data
        # 2 校验参数
        ser = BookSerializer(data=data)
        ser.is_valid(raise_exception=True)
        # 3 保存或者更新
        ser.save()
        # 4 返回数据
        return ser.data

data = {'name':'python'}
BooksViews().post(data)