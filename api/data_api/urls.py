from django.urls import path
from .views import (
        DeleteView,
        ImportView,
        ModelNameListView,
        ModelNameIdView,
        )

urlpatterns = [
        path('import', ImportView.as_view(), name = 'data_import'),
        path('import/', ImportView.as_view()),

        path('detail/<str:model_name>', ModelNameListView.as_view(),
            name = 'detail_model_list'),
        path('detail/<str:model_name>/', ModelNameListView.as_view()),

        path('detail/<str:model_name>/<int:id>', ModelNameIdView.as_view(),
            name = 'detail_model_id'),
        path('detail/<str:model_name>/<int:id>/', ModelNameIdView.as_view()),

        path('deletealldata', DeleteView.as_view(), name='delete_all'),
        path('deletealldata/', DeleteView.as_view()),
        ]
