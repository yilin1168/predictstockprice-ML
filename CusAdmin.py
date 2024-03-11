from django.contrib import admin

class MultiDBModelAdminMixin:
    # 指定用于操作的数据库别名
    using = 'default'

    def save_model(self, request, obj, form, change):
        # 指定对象保存到的数据库
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # 指定从哪个数据库删除对象
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # 修改查询集以使用指定的数据库
        return super().get_queryset(request).using(self.using)




class CustomAdminForDB1(MultiDBModelAdminMixin, admin.ModelAdmin):
    using = 'db1'

class CustomAdminForDB2(MultiDBModelAdminMixin, admin.ModelAdmin):
    using = 'db2'

# 然后注册你的模型和自定义的 ModelAdmin
admin.site.register(MyModel1, CustomAdminForDB1)
admin.site.register(MyModel2, CustomAdminForDB2)


