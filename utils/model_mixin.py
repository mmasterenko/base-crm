import os

from django.db import models


class CreateUpdateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SafeDeleteMixin(models.Model):
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()


class FileMixin:
    @property
    def size(self):
        if self.file:
            return self.file.size
        else:
            return None

    @property
    def filename(self):
        if self.file:
            return os.path.basename(self.file.name)  # cause self.file.name can include upload_dir path
        else:
            return None
