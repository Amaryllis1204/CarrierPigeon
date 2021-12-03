from django.contrib import admin
from .models import AmazonOnlyGoods, AmazonDomainOnlyGoods, AmazonOnlyBrand
# Register your models here.

admin.site.register(AmazonOnlyGoods)
admin.site.register(AmazonDomainOnlyGoods)
admin.site.register(AmazonOnlyBrand)