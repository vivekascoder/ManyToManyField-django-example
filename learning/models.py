from django.db import models


class Tag(models.Model):
    name = models.CharField(verbose_name="Tag Name.",
                            max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(
        verbose_name="Title Of The Post.", max_length=50, null=False, blank=False)
    content = models.TextField(
        verbose_name="Content Of The Post.", null=False, blank=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
