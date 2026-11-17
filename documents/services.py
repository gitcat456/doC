from .models import Document


def create_document(*, owner, validated_data):
    return Document.objects.create(
        owner=owner,
        **validated_data
    )


def get_document(*, owner, document_id):
    return Document.objects.get(
        owner=owner,
        document_id=document_id
    )


def list_documents(*, owner):
    return Document.objects.filter(
        owner=owner
    ).order_by("-created_at")
