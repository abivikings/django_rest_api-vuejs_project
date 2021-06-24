from django.db import models


class Item(models.Model):
    item_name = models.CharField(length=50)
    item_desc = models.CharField(length=100)
    item_price = models.IntegerField(null=True)

    @classmethod
    def get_all_item(cls):
        items = Item.objects.all()
        return items

    @classmethod
    def get_sing_item(cls, id):
        items = Item.objects.filter(id=id)
        return items
