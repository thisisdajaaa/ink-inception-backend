from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class S3BaseStorage(S3Boto3Storage):
    def url(self, name, parameters=None, expire=None, http_method=None):
        url = super().url(
            name, parameters=parameters, expire=expire, http_method=http_method
        )
        if self.custom_domain:
            url = url.replace(self.endpoint_url, self.custom_domain)
        return url


class S3StaticStorage(S3BaseStorage):
    location = settings.STATICFILES_LOCATION


class S3MediaStorage(S3BaseStorage):
    pass
