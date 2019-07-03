from DRF_demo.baseserializer import BaseSerlializer

'''
定义接收字段 以及（）内的参数
'''


class Serlializer(BaseSerlializer):
    def field(self):
        '''定义接收的'''
        pass

    def get_validators(self):
        '''
        外部引用函数
        :return:
        '''
        pass
