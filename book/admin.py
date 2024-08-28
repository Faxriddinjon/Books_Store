from django.contrib import admin

from .models import Author,Book,Purchases   


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Purchases)

# Register your models here.
