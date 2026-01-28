from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import BirthdayForm
from .models import Birthday


class BirthdayMixin:
    model = Birthday
    success_url = reverse_lazy('birthday:list')


class BirthdayFormMixin:
    form_class = BirthdayForm
    template_name = 'birthday/birthday.html'


class BirthdayCreateView(BirthdayMixin, LoginRequiredMixin, BirthdayFormMixin,
                         CreateView):
    pass


class BirthdayUpdateView(BirthdayMixin, LoginRequiredMixin, BirthdayFormMixin,
                         UpdateView):
    pass


class BirthdayDeleteView(BirthdayMixin, LoginRequiredMixin, DeleteView):
    pass


class BirthdayListView(ListView):
    model = Birthday
    # ...сортировку, которая будет применена при выводе списка объектов:
    ordering = 'id'
    # ...и даже настройки пагинации:
    paginate_by = 3


@login_required
def simple_view(request):
    return HttpResponse('Страница для залогиненных пользователей!')
