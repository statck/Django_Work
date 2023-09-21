from django.db import models

# Create your models here.
class UserInfo(models.Model):  # 类名代指数据库中表名
    # 创建类
    name = models.CharField(max_length=32)  # 表中的字段名
    password = models.CharField(max_length=64) # 表中的字段名
    age = models.IntegerField() # 表中的字段名
    """
        create table app01_userinfo(
            id bigint auto_increment primary key
            name varchar(32),
            password varchar(64),
            age int
        )
    """