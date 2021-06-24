from django.db import models


class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_no = models.IntegerField(unique=True)
    item_desc = models.CharField(max_length=100)
    item_price = models.FloatField(null=True)

    @classmethod
    def get_all_item(cls):
        items = Item.objects.all()
        return items

    @classmethod
    def get_sing_item(cls, id):
        items = Item.objects.filter(id=id)
        return items
