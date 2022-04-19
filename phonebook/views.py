from django.shortcuts import render, HttpResponse, redirect
from django import views
from phonebook.forms import ContactForm
from phonebook.models import Contact


# Create views for phonebook
class home(views.generic.TemplateView):
    template_name = 'home.html'


class ContactList(views.generic.ListView):
    # model = Contact
    queryset = Contact.objects.order_by('first_name')
    template_name = 'contacts.html'


class ContactCreate(views.View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'newcontact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # return render(request, 'newcontact.html', {'form': form})
            return redirect('/home/contact/')
        else:
            return render(request, 'newcontact.html', {'form': form.errors})


class ContactUpdate(views.generic.UpdateView):
    model = Contact
    template_name = 'updatecontact.html'
    form_class = ContactForm
    success_url = '/home/contact/'


class ContactDelete(views.generic.DeleteView):
    model = Contact
    template_name = 'deletecontact.html'
    # form_class = ContactForm
    success_url = '/home/contact/'