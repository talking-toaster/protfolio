from django.db import models


class Blog(models.Model):
    objects = models.Manager()
    title = models.CharField(default='标题', max_length=50)
    date = models.DateField()
    image = models.ImageField(default='default.jpg', upload_to='images/')
    text = models.TextField(default='正文', max_length=5000)

    def __str__(self):
        return self.title
