import os
import uuid

from django.utils.text import slugify


def generic_image_upload_to(instance, filename, folder):
    _, file_extension = os.path.splitext(filename)
    slug = slugify(instance.slug)
    new_filename = f"{uuid.uuid4()}{file_extension}"
    return f"{folder}/{slug}-{new_filename}"
