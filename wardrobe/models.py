from django.db import models

# Create your models here.
class MainMenu(models.Model):
    Name = models.CharField(max_length=255,default='无')

class Menu(models.Model):
    Wardrobe = models.ForeignKey(MainMenu,related_name='wardrobe_id')
    User = models.IntegerField(4)#用户
    Menu = models.IntegerField(4)#菜单
    Detail = models.CharField(max_length=30,default='无')#详细描述

    def __str__(self):
        return self.Detail

class Clothes(models.Model):
    Menu = models.ForeignKey(Menu , related_name='menu_id')
    Detail = models.FileField()
    Time = models.DateTimeField()
    Note = models.CharField(max_length=255,default='无')#详细描述

    def __str__(self):
        return self.Detail

    def setClothes(self, Detail, Time):
        self.Detail = Detail
        self.Time = Time