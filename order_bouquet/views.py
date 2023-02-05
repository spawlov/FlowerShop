from decimal import Decimal

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .forms import OrderForm, ConsultationForm
from .models import Bouquet, Category, Consultation, Order


class HomeView(generic.ListView):
    queryset = Bouquet.objects.all().order_by('?')[:3]
    template_name = 'index.html'
    context_object_name = 'home'


class CatalogView(generic.ListView):
    queryset = Bouquet.objects.all().order_by('?')[:6]
    template_name = 'catalog.html'
    context_object_name = 'catalog'


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


class ConsultationView(generic.ListView):
    model = Consultation
    template_name = 'consultation.html'
    context_object_name = 'consultations'


class OrderView(generic.ListView):
    model = Order
    template_name = 'order.html'
    context_object_name = 'orders'


class OrderStepView(generic.ListView):
    model = Order
    template_name = 'order-step.html'
    context_object_name = 'orders-step'


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
