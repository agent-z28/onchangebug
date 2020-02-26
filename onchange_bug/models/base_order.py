from odoo import models, api, fields
import logging

_logger = logging.getLogger(__name__)


class BaseOrder(models.Model):
    _name = "base.order"
    _description = "Base Order"

    name = fields.Char()

    base_order_tour_ids = fields.One2many("base.order.tour", "base_order_id")
    base_order_cost_ids = fields.One2many("base.order.cost", "base_order_id")


class BaseOrderTour(models.Model):
    _name = "base.order.tour"
    _description = "Base Order Tour"

    base_order_id = fields.Many2one("base.order")
    distance = fields.Float()


class BaseOrderCost(models.Model):
    _name = "base.order.cost"
    _description = "Base Order Cost"

    base_order_id = fields.Many2one("base.order")
    base_order_tour_id = fields.Many2one("base.order.tour")

    @api.depends(
        "base_order_id.base_order_tour_ids",
        "base_order_tour_id",
        "base_order_tour_id.distance",
    )
    def _get_price(self):
        print("shalalalalal")
        for rec in self:
            rec.price = rec.base_order_tour_id.distance * 10
            _logger.info("_get_price results in %s", rec.price)

    price = fields.Float(store=True, compute="_get_price")
