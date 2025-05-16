from django.contrib import admin
from .models import Category, Tag, Product, Offer, WishList, Image

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class OfferInline(admin.StackedInline):
    model = Offer
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'state', 'condition', 'price', 'user', 'create_date')
    list_filter = ('category', 'state', 'condition', 'user')
    search_fields = ('name', 'description', 'category__name', 'user__username')
    inlines = [ImageInline, OfferInline]
    filter_horizontal = ('tags',)

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'category', 'tags', 'condition', 'state', 'price')
        }),
        ('Relations', {
            'fields': ('user', 'ubicacion')
        }),
        ('Dates', {
            'fields': ('create_date', 'update_date')
        }),
    )
    readonly_fields = ('create_date', 'update_date')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)
    list_filter = ('category',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('product', 'offer_price', 'start_date', 'end_date', 'active')
    list_filter = ('active',)
    search_fields = ('product__name',)

@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'create_date')
    search_fields = ('user__username', 'product__name')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'url', 'order')
    search_fields = ('product__name',)
    list_filter = ('product',)
