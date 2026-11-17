from django.conf import settings
from django.db import models


class Document(models.Model):
    document_id = models.BigAutoField(primary_key=True)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="documents"
    )

    title = models.CharField(max_length=255)
    doc_type = models.CharField(max_length=50)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
