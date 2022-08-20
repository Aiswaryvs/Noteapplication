from django.urls import path
from notes import views

urlpatterns = [
    path("note/add",views.CreateNoteView.as_view(),name="add-notes"),
    path("note/change/<int:id>",views.NotesUpdateView.as_view(),name="update-notes"),
    path("home", views.IndexView.as_view(),name="home"),
    path('remove/<int:id>',views.remove_notes,name="note-delt"),


]