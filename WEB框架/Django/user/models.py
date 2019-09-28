from django.db import models

# Create your models here.
class UserBaseInfo(models.Model):
    # 使用内部 Meta类 来给模型赋予元数据，就像：
    class Meta:
        # 数据库表名
        db_table = "user_base_info"

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, null=False)
    age = models.IntegerField(null=False)

    def __repr__(self):
        return "".format(self.id, self.username, self.age)

    __str__ = __repr__
