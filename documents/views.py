from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import DocumentSerializer
from .services import (
    create_document,
    get_document,
    list_documents,
)


@api_view(["POST", "GET"])
@permission_classes([IsAuthenticated])
def document_list_create(request):

    if request.method == "POST":
        serializer = DocumentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        document = create_document(
            owner=request.user,
            validated_data=serializer.validated_data
        )

        return Response(
            DocumentSerializer(document).data,
            status=status.HTTP_201_CREATED
        )

    documents = list_documents(owner=request.user)
    serializer = DocumentSerializer(documents, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def document_detail(request, document_id):

    try:
        document = get_document(
            owner=request.user,
            document_id=document_id
        )
    except Document.DoesNotExist:
        return Response(
            {"error": "Document not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = DocumentSerializer(document)

    return Response(serializer.data, status=status.HTTP_200_OK)
