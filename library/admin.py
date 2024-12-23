from django.contrib import admin

from library.models import *

# Register your models here.
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Borrow)