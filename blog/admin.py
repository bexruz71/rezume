from django.contrib import admin
from .models import Brand,Portfolio,Discount,Resume,Awards,About,Comment,Service,Blog,Contact

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')

@admin.register(Awards)
class AwardsAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','author_name')
    list_display_links = ('id','author_name')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')

















