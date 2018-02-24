from rest_framework.generics import ListCreateAPIView

from utils.rest_generics import RUDAPIView
from .models import IncomeNExpense, MoneyFlow


class IEList(ListCreateAPIView):
    pass


class IEDetail(RUDAPIView):
    pass


class MoneyFlowList(ListCreateAPIView):
    pass


class MoneyFlowDetail(RUDAPIView):
    pass
