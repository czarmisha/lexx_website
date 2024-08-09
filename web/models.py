from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Image(AbstractModel):
    image = models.ImageField(upload_to="images/")

    def __str__(self) -> str:
        return f"Image {str(self.pk)} - {self.image}"


class Post(TranslatableModel, AbstractModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=100),
        content=models.TextField(),
    )
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Application(AbstractModel):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.pk}: {self.name} {self.phone}"
