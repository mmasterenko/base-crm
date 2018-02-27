from django.db import models

from project.utils.model_mixin import AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin


class GoodsFlow(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    перемещения товаров внутри аккаунта
    """
    pass

    class Meta:
        db_table = 'goods_flow'


class GoodsIn(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    поступления товара извне
    """
    pass

    class Meta:
        db_table = 'goods_in'


class GoodsOut(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    отгрузка товара во вне
    """
    pass

    class Meta:
        db_table = 'goods_out'


class PurchaseOrder(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    заказ поставщику
    """
    pass

    class Meta:
        db_table = 'purchase_order'


class RefundCustomer(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    возвраты покупателю
    """
    pass

    class Meta:
        db_table = 'refund_customer'


class RefundProvider(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    возвраты поставщику
    """
    pass

    class Meta:
        db_table = 'refund_provider'


class Inventorisation(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    инвентаризация
    """
    pass

    class Meta:
        db_table = 'inventorisation'


class InventoryOut(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    списание товаров (по итогам инвентаризации)
    """
    pass

    class Meta:
        db_table = 'inventory_out'


class InventoryIn(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    оприходование товара (по итогам инвентаризации)
    """
    pass

    class Meta:
        db_table = 'inventory_in'
