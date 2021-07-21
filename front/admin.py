from django.contrib import admin

# Register your models here.
from front.models import Menu, Tag, Page, News

admin.site.register(Menu)
admin.site.register(Tag)
admin.site.register(Page)
admin.site.register(News)