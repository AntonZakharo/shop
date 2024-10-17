from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    pass


class Item(models.Model):
    image = models.ImageField(_('Изображение'), upload_to='images/', blank=True, null=True, default='images/default.png')
    BOOK = 'book'
    COMIC = 'comic'
    ITEM_TYPE_CHOICES = [(BOOK, _('Книга')), (COMIC, _('Комикс'))]
    title = models.CharField(_('Название'), max_length=255)
    price = models.DecimalField(_('Цена'), max_digits=10, decimal_places=2)
    stock = models.IntegerField(_('Количество'))
    item_type = models.CharField(_('Тип'), max_length=10, choices=ITEM_TYPE_CHOICES)
    author = models.CharField(_('Автор'), max_length=255)
    genre = models.CharField(_('Жанр'), max_length=100)
    publish_date = models.DateField(_('Дата публикации'))
    description = models.TextField(_('Описание'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')


class ShoppingCartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.item.title} x{self.quantity} (User: {self.user.username})"

