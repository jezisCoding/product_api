from django.urls import path, include
from .views import (
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
        ]
