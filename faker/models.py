from django.db import models


class Servant(models.Model):
    No = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=20)
    classname = models.CharField(max_length=10, choices=(('Saber', '剑士'), ('Archer', '弓兵'), ('Lancer', '枪兵'),
                                                         ('Assassin', '暗匿着'), ('Rider', '骑兵'), ('Caster', '魔术师'),
                                                         ('Ruler', '裁定者'), ('MoonCancer', '月癌'),
                                                         ('Avenger', '复仇者'), ('Alterego', '他人格'),
                                                         ('Foreigner', '降临者'), ('Berserker', '狂战士'),
                                                         ('Shielder', '盾兵')))
    nickname = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, choices=(('male', '男'), ('female', '女'), ('unknown', '未知')),
                              default='female', verbose_name='性别')

    def __str__(self):
        return self.name



class Story(models.Model):
    storyno = models.IntegerField(primary_key=True)
    text = models.TextField()
    sno = models.ForeignKey("Servant", on_delete=models.CASCADE)

    def __str__(self):
        return self.storyno
