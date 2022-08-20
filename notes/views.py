from django.shortcuts import render,redirect
from notes.models import Notes
from django.views.generic import View,CreateView,UpdateView
from django.urls import reverse_lazy
from notes.forms import NotesForm
from django.contrib import messages




class CreateNoteView(CreateView):
    model = Notes
    template_name = "addnote.html"
    form_class = NotesForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Note has been Added")
        self.object = form.save()
        return super().form_valid(form)


class IndexView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = reverse_lazy("home")
    template_name = "home.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nts = Notes.objects.all().order_by("-created_at")
        context["notes"] = nts
        return context




class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    template_name = "notesupdate.html"
    success_url = reverse_lazy("home")
    pk_url_kwarg = "id"

    def form_valid(self, form):
        messages.success(self.request, "notes has been Updated")
        self.object = form.save()
        return super().form_valid(form)

def remove_notes(request,*args,**kwargs):
    id=kwargs.get("id")
    nte=Notes.objects.get(id=id)
    form=NotesForm(instance=nte)
    nte.delete()
    messages.success(request,"note has been removed")
    return redirect("home")




