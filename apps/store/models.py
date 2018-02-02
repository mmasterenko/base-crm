from django.db import models

from project.utils.model_mixin import AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin


class GoodsFlow(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    перемещения товаров внутри аккаунта
    """
    pass


class GoodsReceipt(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    поступления товара извне
    """
    pass


class GoodsOutbound(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    отгрузка товара во вне
    """
    pass


class PurchaseOrder(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    заказ поставщику
    """
    pass


class RefundToCustomer(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    возвраты покупателю
    """
    pass


class RefundToProvider(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    возвраты поставщику
    """
    pass


class Inventory(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    инвентаризация
    """
    pass


class GoodsWriteOff(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    списание товаров (по итогам инвентаризации)
    """
    pass


class GoodsPlacingIn(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    оприходование товара (по итогам инвентаризации)
    """
    pass
