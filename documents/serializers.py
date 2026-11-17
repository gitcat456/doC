from rest_framework import serializers
from .models import Document


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = [
            "document_id",
            "title",
            "doc_type",
            "content",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "document_id",
            "created_at",
            "updated_at",
        ]

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Title cannot be empty."
            )
        return value

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Content cannot be empty."
            )
        return value
