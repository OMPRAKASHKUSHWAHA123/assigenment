from odoo import models,fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'


    def action_confirm(self):
        res = super().action_confirm()
        for order in self:
            for picking in order.picking_ids:
                if picking.picking_type_code == "outgoing":
                    picking.tag_ids = [(6, 0, order.tag_ids.ids)]
        return res
        


