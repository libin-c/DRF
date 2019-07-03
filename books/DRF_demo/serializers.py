from DRF_demo.serializer import Serlializer


class BookSerializer(Serlializer):
    def validate(self, attrs):
        '''
        验证字段
        :param attrs:  是views视图函数中date 接收的dict
        :return:
        '''
        # 返回字段
        print("验证操作")
        return attrs

    def create(self, validated_data):
        '''
        保存数据
        :param validated_data: 验证后的数据ser.validated_data
        :return:
        '''

        # 返回保存后的图书对象
        return 'create'

    def update(self, instance, validated_data):
        '''
        更新数据
        :param instance: 更新的图书对象
        :param validated_data: 更新的数据
        :return:
        '''
        return 'update'
