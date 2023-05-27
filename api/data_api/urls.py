from django.urls import path
from .views import (
        DeleteView,
        ImportView,
        ModelNameListView,
        ModelNameIdView,
        )

urlpatterns = [
        path('import', ImportView.as_view()),
        path('import/', ImportView.as_view()),

        path('detail/<str:model_name>', ModelNameListView.as_view()),
        path('detail/<str:model_name>/', ModelNameListView.as_view()),

        path('detail/<str:model_name>/<int:id>', ModelNameIdView.as_view()),
        path('detail/<str:model_name>/<int:id>/', ModelNameIdView.as_view()),

        path('deletealldata', DeleteView.as_view()),
        path('deletealldata/', DeleteView.as_view()),
        ]
