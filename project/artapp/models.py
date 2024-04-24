from django.db import models
CATEGORY_CHOICES=(
    ('PP','Pencil Portrait'),
    ('CP','Colour Portrait'),
    ('C','Caricatures'),
    ('CW','Custom Works'),
)

class Art(models.Model):
    category=models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='art_images')

    def __str__(self):
        return self.description
