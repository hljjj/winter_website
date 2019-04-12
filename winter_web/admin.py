from django.contrib import admin

from winter_web.models import Topic,Entry #导入类topic

# Register your models here.

admin.site.register(Topic) #调用admin模块的方法注册topic
admin.site.register(Entry)
