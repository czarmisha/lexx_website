from django.db import models


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Image(AbstractModel):
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title


class Post(AbstractModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Application(AbstractModel):
    fio = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.phone
