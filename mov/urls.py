from django.urls import path, include
from .views import HomeListView, CategoryListView,MovieDetailView,MovieTypeView

app_name = 'mov'
urlpatterns = [
    path('', HomeListView.as_view(), name="all_movies"),
    path('type/<str:type>/', MovieTypeView.as_view(), name="movies_type_view"),
    path('category/<str:category>/', CategoryListView.as_view(), name="movies_list_by_category"),
    path('details/<str:type>/<str:slug>/<str:production>/',MovieDetailView.as_view(),name="movie_detail")
]
