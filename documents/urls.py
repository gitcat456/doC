from django.urls import path
from . import views

urlpatterns = [
    path(
        "documents/",
        views.document_list_create,
        name="document-list-create"
    ),
    path(
        "documents/<int:document_id>/",
        views.document_detail,
        name="document-detail"
    ),
]
