from django.db import models
#引入ckeditor的富文本编辑器
#引入ckeditor富文本编辑器
from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
# # django 2.0以后foreignkey需要有on delete属性，同时不用关键词to

# 分类表
class Category(models.Model):
    name = models.CharField(max_length=24, verbose_name="名称")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = verbose_name = "分类表"


# 文章表
class Articles(models.Model):
    img = models.ImageField(verbose_name='首图', upload_to='articles')
    title = models.CharField(max_length=24, verbose_name='标题')
    category = models.ForeignKey('Category', verbose_name="分类",on_delete=models.CASCADE)
    desc = models.CharField(max_length=128, verbose_name="描述")
    time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    content = RichTextField(verbose_name="内容", config_name='ck')
    # 富文本编辑器（支持图片上传）
    # content = RichTextUploadingField(verbose_name="内容", config_name='ck')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = verbose_name = "文章表"


# 相册表
class Album(models.Model):
    img = models.ImageField(verbose_name="首图", upload_to='album')
    position = models.CharField(max_length=24, verbose_name="地点")
    desc = models.CharField(max_length=128, verbose_name="描述")
    content = RichTextField(verbose_name="内容", config_name='ck')

    def __str__(self):
        return "{}:{}".format(self.position, self.content)

    class Meta:
        verbose_name_plural = verbose_name = "相册表"

# 用户表
class Users(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=24)
    password = models.CharField(max_length=72, verbose_name="密码")
    avatar = models.ImageField(verbose_name="头像", upload_to='avatar')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = verbose_name = "用户表"


# 留言表
class Leave(models.Model):
    time = models.DateTimeField(auto_now_add=True, verbose_name="时间")
    content = models.CharField(max_length=128, verbose_name="内容")
    user = models.ForeignKey('Users', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = verbose_name = "留言表"