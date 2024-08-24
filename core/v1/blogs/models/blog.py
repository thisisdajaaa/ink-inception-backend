import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone

from ....utils.helpers.files import generic_image_upload_to


class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    main_image = models.ImageField(
        upload_to=lambda instance, filename: generic_image_upload_to(
            instance, filename, "blog-images"
        ),
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blogs",
    )

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self._state.adding and self.pk:
            old_instance = Blog.objects.get(pk=self.pk)
            if old_instance.main_image and old_instance.main_image != self.main_image:
                old_instance.main_image.delete(save=False)
        super(Blog, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.main_image:
            self.main_image.delete(save=False)
        super(Blog, self).delete(*args, **kwargs)

    @property
    def title_changed(self):
        original = Blog.objects.filter(pk=self.pk).first()
        if original:
            return original.title != self.title
        return False
