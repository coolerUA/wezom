from django.db import models

from django.contrib.auth.models import User

from django.utils.safestring import mark_safe

from image_cropping.fields import ImageRatioField, ImageCropField
from easy_thumbnails.files import get_thumbnailer
from pyback.settings import THUMBNAIL_HEIGTH, THUMBNAIL_WIDTH


class Category(models.Model):
    name = models.CharField(max_length=250, default='')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return '%s (%s)' % (self.name, self.category)


class Product(models.Model):
    name = models.CharField(max_length=250, default='')
    image = models.ImageField(upload_to='product', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    consist = models.TextField(max_length=250, default='')
    price = models.FloatField(max_length=10, default=0)

    @property
    def image_tag(self):
        return mark_safe('<img src="%s" />' % self.image.url)

    def __str__(self):
        return '%s (%s)' % (self.name, self.category)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    @property
    def product_thumbnail(self):
        try:
            return get_thumbnailer(self.image).get_thumbnail({
                'size': (THUMBNAIL_HEIGTH, THUMBNAIL_WIDTH),
                'box': (THUMBNAIL_HEIGTH, THUMBNAIL_WIDTH),
                'crop': 'smart',
            }).url
        except:
            return 'noimage.png'
