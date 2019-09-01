from django.db import models


class Gallery(models.Model):
    objects = models.Manager()
    title = models.CharField(default='标题', max_length=50)

    image = models.ImageField(default='default.jpg', upload_to='images/')
    description = models.CharField(default='摘要', max_length=50)

    def __str__(self):
        return self.title
