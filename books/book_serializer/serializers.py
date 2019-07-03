from rest_framework import serializers

from book.models import BookInfo


class HeroSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    hname = serializers.CharField()
    hgender = serializers.IntegerField()
    hcomment = serializers.CharField()


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)  # read_only 指定该字段只参加序列坏过程
    btitle = serializers.CharField(min_length=3, max_length=10, validators='')
    bpub_date = serializers.DateField(write_only=True)  # write_only 指定该字段只参加反序列坏过程
    bread = serializers.IntegerField()  # default = 10 默认   required=False 不是比传字段
    bcomment = serializers.IntegerField(min_value=1, max_value=200)
    is_delete = serializers.BooleanField()

    # 01 嵌套序列化返回 用关联查询的字段作为序列化器的字段，根据所指定的序列化器字段返回内容
    # heroinfo_set = HeroSerializer(many=True)
    # 02 返回关联数据的id 值
    # heroinfo_set = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # 03 返回关联数据的__str__(self):方法
    # heroinfo_set = serializers.StringRelatedField(many=True, read_only=True)
    def validate_btitle(self, attrs):
        '''
        验证单一字段  固定方法名 , 不固定参数名称
        :param attrs: btitle 字段
        :return:
        '''
        if attrs == 'python':
            raise serializers.ValidationError("图书名称不能为python!!")
        # 返回字段
        return attrs

    def validate(self, attrs):
        '''
        验证多个字段 固定方法名, 不固定参数名称
        :param attrs:  是views视图函数中date 接收的dict
        :return:
        '''
        if attrs['bread'] > attrs['bcomment']:
            raise serializers.ValidationError("阅读量不能大于评论量")
        # 返回字段
        return attrs

    def create(self, validated_data):
        '''
        保存数据
        :param validated_data: 验证后的数据ser.validated_data
        :return:
        '''
        book = BookInfo.objects.create(**validated_data)
        # 返回保存后的图书对象
        return book

    def update(self, instance, validated_data):
        '''
        更新数据
        :param instance: 更新的图书对象
        :param validated_data: 更新的数据
        :return:
        '''
        instance.btitle = validated_data.get('btitle')
        instance.save()
        return instance


class BookMedolSerializer(serializers.ModelSerializer):
    """图书数据序列化器"""
    # 04  显示指明字段
    sms_code = serializers.IntegerField(min_value=8, max_value=8, read_only=True)

    class Meta:
        model = BookInfo
        # 01   全部字段
        fields = '__all__'
        # 02  包含字段
        # fields = ('id', 'btitle', 'bread')
        # 03  不包含字段
        # exclude = ('id',)

        # 05    read_only 字段 只参与序列化字段 只对ModelSerializer 未指明字段有效
        # read_only_fields = ('btitle', 'bread', 'bcomment')
        # 06    extra_kwargs 添加额外参数
        extra_kwargs = {
            'bread': {'min_value': 0},
            'bcomment': {'min_value': 1, 'max_value': 200}
        }

    def validate_btitle(self, attrs):
        '''
        验证单一字段  固定方法名 , 不固定参数名称
        :param attrs: btitle 字段
        :return:
        '''
        if attrs == 'python':
            raise serializers.ValidationError("图书名称不能为python!!")
        # 返回字段
        return attrs

    def validate(self, attrs):
        if attrs['bread'] > attrs['bcomment']:
            raise serializers.ValidationError("阅读量不能大于评论量")
            # 返回字段
        return attrs
