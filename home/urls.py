from django.urls import path
from home.views import home_view, add_book, edit_book, AddBookView

app_name = 'app'

urlpatterns = [
    path("home/", home_view, name="home"),
    path("add_book/", AddBookView.as_view() , name="add_book"),
    path("edit_book/<int:book_id>/", edit_book, name="edit_book"),
]