import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone


class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    main_image = models.ImageField(upload_to="blogs/images/", blank=True, null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blogs",
    )

    class Meta:
        ordering = ["-created_at"]

    @property
    def title_changed(self):
        original = Blog.objects.filter(pk=self.pk).first()
        if original:
            return original.title != self.title
        return False
