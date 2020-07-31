from django.contrib import admin
from test1.models import File_Upload
# Register your models here.
# class File_Upload_Admin(admin.ModelAdmin):
#     class Meta:
#         model=File_Upload
#         fields="__all__"
admin.site.register(File_Upload)