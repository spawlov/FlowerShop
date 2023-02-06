import phonenumbers

from decimal import Decimal
from typing import Any
from django.http import HttpRequest, HttpResponse

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.db.models import Count

from .forms import OrderForm, ConsultationForm
from .models import Bouquet, Category, Consultation, Order, Client


class HomeView(generic.ListView):
    queryset = Bouquet.objects.all().order_by('?')[:3]
    template_name = 'index.html'
    context_object_name = 'home'

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        fname = request.POST.get('fname')
        tel = request.POST.get('tel')
        consultation = Consultation(name=fname, phone=tel)
        consultation.save()
        context = {'created': True}
        return render(request, 'consultation_confirm.html', context)


class CatalogView(generic.ListView):
    queryset = Bouquet.objects.all()
    template_name = 'catalog.html'
    context_object_name = 'catalog'
    paginate_by = 9


class QuizView(generic.ListView):
    model = Category
    template_name = 'quiz.html'
    context_object_name = 'categories'


class QuizStepView(generic.ListView):
    model = Bouquet
    template_name = 'quiz-step.html'
    context_object_name = 'quiz_step'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat'] = self.request.GET.get('cat', 0)
        return context


class ResultView(generic.ListView):
    model = Bouquet
    template_name = 'result.html'
    context_object_name = 'results'

    def get_queryset(self):
        cat_id = int(self.request.GET.get('cat'))
        price_choice = self.request.GET.get('price')

        if cat_id:
            queryset = Bouquet.objects.filter(
                category=cat_id
            ).order_by('-price')
        else:
            queryset = Bouquet.objects.all().order_by('-price')

        if price_choice == '1000':
            queryset = queryset.filter(price__lte=Decimal(1000))
        elif price_choice == '1000:5000':
            queryset = queryset.filter(
                price__gt=Decimal(1000), price__lte=Decimal(5000)
            )
        elif price_choice == '5000':
            queryset = queryset.filter(price__gt=Decimal(5000))

        return queryset


class ConsultationView(generic.CreateView):
    form_class = ConsultationForm
    model = Consultation
    template_name = 'consultation.html'
    context_object_name = 'consultations'

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        fname = request.POST.get('fname')
        tel = request.POST.get('tel')
        consultation = Consultation(name=fname, phone=tel)
        consultation.save()
        context = {'created': True}
        return render(request, 'consultation_confirm.html', context)


class OrderView(generic.TemplateView):
    template_name = 'order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['bouquet'] = self.request.GET.get('bouquet')
        return context


class OrderStepView(generic.View):
    def post(self, request, *args, **kwargs):
        delivery_times = {
            'Как можно скорее': 'AS_SOON_AS_POSSIBLE',
            'с 10:00 до 12:00': 'FROM_10_TO_12',
            'с 12:00 до 14:00': 'FROM_12_TO_14',
            'с 14:00 до 16:00': 'FROM_14_TO_16',
            'с 16:00 до 18:00': 'FROM_16_TO_18',
            'с 18:00 до 20:00': 'FROM_18_TO_20',
        }

        client, created = Client.objects.get_or_create(
            name=self.request.POST.get('fname'),
            phone=phonenumbers.parse(self.request.POST.get('tel')),
        )

        min_orders_count = min(list(
            User.objects.filter(is_staff=False).annotate(
                c=Count('courier_orders')
            ).values_list('c', flat=True)
        ))
        min_count_orders_courier = User.objects.annotate(c=Count('courier_orders')).filter(
            is_staff=False,
            c=min_orders_count
        ).first()

        Order.objects.create(
            bouquet=Bouquet.objects.get(pk=self.request.GET.get('bouquet')),
            manager=User.objects.filter(is_staff=True).last(),
            courier=min_count_orders_courier,
            client=client,
            address=self.request.POST.get('adres'),
            status='NOT_PAID',
            delivery_time=delivery_times[self.request.POST.get('orderTime')],
        )

        return render(self.request, 'order-step.html')


class CardView(generic.DetailView):
    model = Bouquet
    template_name = 'card.html'
    context_object_name = 'card'


class AdminOrdersList(LoginRequiredMixin, generic.ListView):
    model = Order
    ordering = ['-pk']
    template_name = 'admin_order.html'
    context_object_name = 'admin_orders'
    paginate_by = 10


class AdminOrderAdd(LoginRequiredMixin, generic.CreateView):
    form_class = OrderForm
    model = Order
    template_name = 'order_edit.html'
    context_object_name = 'order_data'
    success_url = reverse_lazy('orders-list')


class AdminOrderEdit(LoginRequiredMixin, generic.UpdateView):
    form_class = OrderForm
    model = Order
    template_name = 'order_edit.html'
    context_object_name = 'order_data'
    success_url = reverse_lazy('orders-list')


class AdminConsultationList(LoginRequiredMixin, generic.ListView):
    model = Consultation
    ordering = ['-pk']
    template_name = 'admin_consultation.html'
    context_object_name = 'consultations'
    paginate_by = 10


class AdminConsultationEdit(LoginRequiredMixin, generic.UpdateView):
    form_class = ConsultationForm
    model = Consultation
    template_name = 'consultation_edit.html'
    context_object_name = 'consultation_data'
    success_url = reverse_lazy('consultations-list')
