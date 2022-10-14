from django.db import models


class WbData(models.Model):
    article = models.CharField(max_length=30, unique=True, blank=True, null=True)
    brand = models.CharField(max_length=250, blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.article


class WbDataFile(models.Model):
    article = models.CharField(max_length=30, blank=True, null=True)
    file = models.FileField(upload_to='files', blank=True, null=True)

    def __str__(self):
        return self.article
