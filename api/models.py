from django.db import models
from imagekit.models import ImageSpecField
from django_extensions.db.fields import AutoSlugField
from imagekit.processors import ResizeToFill, TrimBorderColor, Adjust

# Create your models here.
class Pictures(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title', unique=True, max_length=50)
    image = models.ImageField(upload_to='topic', null=True, blank=True)
    image_large = ImageSpecField(source='image', processors=[ResizeToFill(1440, 900), Adjust(contrast=1.2, sharpness=1.1), TrimBorderColor()], format='JPEG', options={'quality': 70})
    image_medium = ImageSpecField(source='image', processors=[ResizeToFill(1280, 720), Adjust(contrast=1.2, sharpness=1.1), TrimBorderColor()],  format='JPEG', options={'quality': 70})
    image_small = ImageSpecField(source='image', processors=[ResizeToFill(1024, 1024), Adjust(contrast=1.2, sharpness=1.1), TrimBorderColor()], format='JPEG', options={'quality': 70})

    def __str__(self):
        return str(self.title)
