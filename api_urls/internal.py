from django.http import HttpResponse
from django.urls import path

from apps.crm.rest import views as crm_views


app_name = 'internal-api'

urlpatterns = [
    # account and users
    path('account',  lambda r: HttpResponse('OK'), name='account'),
    path('user/<int:pk>',  lambda r: HttpResponse('OK'), name='user-detail'),
    path('user',           lambda r: HttpResponse('OK'), name='user-list'),

    # finance
    path('money-flow/<int:pk>',         lambda r: HttpResponse('OK'), name='money-flow-detail'),
    path('money-flow',                  lambda r: HttpResponse('OK'), name='money-flow-list'),

    path('income-n-expense/<int:pk>',   lambda r: HttpResponse('OK'), name='income-n-expense-detail'),
    path('income-n-expense',            lambda r: HttpResponse('OK'), name='income-n-expense-list'),

    # CRM
    path('task/<int:pk>',         lambda r: HttpResponse('OK'), name='task-detail'),
    path('task',                  lambda r: HttpResponse('OK'), name='task-list'),

    path('request/<int:pk>', crm_views.CustomerRequestDetailView.as_view(), name='request-detail'),
    path('request', crm_views.CustomerRequestListView.as_view(), name='request-list'),

    path('order/<int:pk>',   lambda r: HttpResponse('OK'), name='order-detail'),
    path('order',            lambda r: HttpResponse('OK'), name='order-list'),

    path('order-line/<int:pk>',   lambda r: HttpResponse('OK'), name='order-line-detail'),
    path('order-line',            lambda r: HttpResponse('OK'), name='order-line-list'),

    path('bill/<int:pk>',   lambda r: HttpResponse('OK'), name='bill-detail'),
    path('bill',            lambda r: HttpResponse('OK'), name='bill-list'),

    path('bill-line/<int:pk>',   lambda r: HttpResponse('OK'), name='bill-line-detail'),
    path('bill-line',            lambda r: HttpResponse('OK'), name='bill-line-list'),

    path('voice-call/<int:pk>',   lambda r: HttpResponse('OK'), name='voice-call-detail'),
    path('voice-call',            lambda r: HttpResponse('OK'), name='voice-call-list'),

    # refbook
    path('organisation/<int:pk>',   lambda r: HttpResponse('OK'), name='organisation-detail'),
    path('organisation',            lambda r: HttpResponse('OK'), name='organisation-list'),

    path('shop/<int:pk>',   lambda r: HttpResponse('OK'), name='shop-detail'),
    path('shop',            lambda r: HttpResponse('OK'), name='shop-list'),

    path('counter-agent/<int:pk>',   lambda r: HttpResponse('OK'), name='counter-agent-detail'),
    path('counter-agent',            lambda r: HttpResponse('OK'), name='counter-agent-list'),

    path('product/<int:pk>',   lambda r: HttpResponse('OK'), name='product-detail'),
    path('product',            lambda r: HttpResponse('OK'), name='product-list'),

    path('cash-n-account/<int:pk>',   lambda r: HttpResponse('OK'), name='ca-detail'),
    path('cash-n-account',            lambda r: HttpResponse('OK'), name='ca-list'),

    path('order-status/<int:pk>',   lambda r: HttpResponse('OK'), name='order-status-detail'),
    path('order-status',            lambda r: HttpResponse('OK'), name='order-status-list'),

    path('task-status/<int:pk>',   lambda r: HttpResponse('OK'), name='task-status-detail'),
    path('task-status',            lambda r: HttpResponse('OK'), name='task-status-list'),

    path('request-status/<int:pk>',   lambda r: HttpResponse('OK'), name='request-status-detail'),
    path('request-status',            lambda r: HttpResponse('OK'), name='request-status-list'),

    path('payment-type/<int:pk>',   lambda r: HttpResponse('OK'), name='payment-type-detail'),
    path('payment-type',            lambda r: HttpResponse('OK'), name='payment-type-list'),

    path('price-type/<int:pk>',   lambda r: HttpResponse('OK'), name='price-type-detail'),
    path('price-type',            lambda r: HttpResponse('OK'), name='price-type-list'),

    path('ie-source/<int:pk>',   lambda r: HttpResponse('OK'), name='ie-source-detail'),
    path('ie-source',            lambda r: HttpResponse('OK'), name='ie-source-list'),

    path('ordering-method/<int:pk>',   lambda r: HttpResponse('OK'), name='ordering-method-detail'),
    path('ordering-method',            lambda r: HttpResponse('OK'), name='ordering-method-list'),

    path('ordering-source/<int:pk>',   lambda r: HttpResponse('OK'), name='ordering-source-detail'),
    path('ordering-source',            lambda r: HttpResponse('OK'), name='ordering-source-list'),

    path('unit/<int:pk>',   lambda r: HttpResponse('OK'), name='unit-detail'),
    path('unit',            lambda r: HttpResponse('OK'), name='unit-list'),

    path('counter-agent-group/<int:pk>',   lambda r: HttpResponse('OK'), name='counter-agent-group-detail'),
    path('counter-agent-group',            lambda r: HttpResponse('OK'), name='counter-agent-group-list'),

    path('counter-agent-segment/<int:pk>',   lambda r: HttpResponse('OK'), name='counter-agent-segment-detail'),
    path('counter-agent-segment',            lambda r: HttpResponse('OK'), name='counter-agent-segment-list'),
]
