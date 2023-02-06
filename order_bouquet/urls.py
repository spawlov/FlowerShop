from django.urls import path

from .views import HomeView, CatalogView, QuizView, QuizStepView, ResultView, \
    ConsultationView, OrderView, OrderStepView, CardView, AdminOrdersList, \
    AdminOrderEdit, AdminOrderAdd, AdminConsultationList, AdminConsultationEdit

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('quiz/', QuizView.as_view(), name='quiz'),
    path('quiz-step/', QuizStepView.as_view(), name='quiz_step'),
    path('result/', ResultView.as_view(), name='result'),
    path('consultation/', ConsultationView.as_view(), name='consultation'),
    path('order/', OrderView.as_view(), name='order'),
    path('order-step/', OrderStepView.as_view(), name='order-step'),
    path('card/<int:pk>/', CardView.as_view(), name='card'),

    path('admin-order/', AdminOrdersList.as_view(), name='orders-list'),
    path('order-add/', AdminOrderAdd.as_view(), name='order-add'),
    path('order-edit/<int:pk>/', AdminOrderEdit.as_view(), name='order-edit'),
    path(
        'admin-consultations/',
        AdminConsultationList.as_view(),
        name='consultations-list'
    ),
    path(
        'consultation-edit/<int:pk>/',
        AdminConsultationEdit.as_view(),
        name='consultation-edit'
    ),
]
