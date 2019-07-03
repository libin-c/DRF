#  框架源代码序列化

class BaseSerlializer(object):
    def __init__(self, instance=None, data=None):
        self.instance = instance
        self.validated_data = data

    def is_valid(self, raise_exception=False):
        '''
        验证方法
        :param raise_exception:
        :return:
        '''
        self.validated_data = self.validate(self.validated_data)
        return self.validated_data

    def save(self):
        '''
        保存或者更新
        :return:
        '''
        if self.instance is not None:
            self.instance = self.update(self.instance, self.validated_data)
        else:
            self.instance = self.create(self.validated_data)

    @property
    def data(self):
        '''
        构造序列化结果
        :return:
        '''
        return self.instance

    @property
    def error(self):
        '''
        验证错误
        :return:
        '''
        pass

    def validate(self, attrs):
        '''
        验证
        :param attrs:
        :return:
        '''
        pass

    def create(self, validated_data):
        '''
        保存数据
        :param validated_data: 验证后的数据ser.validated_data
        :return:
        '''

        # 返回保存后的图书对象
        pass

    def update(self, instance, validated_data):
        '''
        更新数据
        :param instance: 更新的图书对象
        :param validated_data: 更新的数据
        :return:
        '''
        pass
