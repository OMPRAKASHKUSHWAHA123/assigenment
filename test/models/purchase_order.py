from odoo import models, api,fields
from collections import defaultdict


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'



    category_id = fields.Many2one('product.category', string='Product Category', )

    @api.model
    def _prepare_purchase_order(self, company, supplier, origin, vals):
        """Group POs by category during procurement."""
        category = vals.get('category_id')
        return {
            'partner_id': supplier.id,
            'company_id': company.id,
            'currency_id': supplier.property_purchase_currency_id.id,
            'origin': origin,
            'date_order': fields.Datetime.now(),
            'category_id': category, 
        }

class StockRuleInherit(models.Model):
    _inherit = 'stock.rule'

    def _make_po_get_domain(self, company, supplier, values):
        """Override PO domain logic to include category"""
        domain = super()._make_po_get_domain(company, supplier, values)
        category_id = values.get('category_id')
        if category_id:
            domain += [('category_id', '=', category_id)]
        return domain


class PurchaseOrderLineSplitByCategory(models.Model):
    _inherit = 'purchase.order.line'

    @api.model
    def _prepare_purchase_order_line(self, product, qty, uom, price_unit, name, po, values, taxes):
        """Add category to values to use in PO grouping"""
        res = super()._prepare_purchase_order_line(product, qty, uom, price_unit, name, po, values, taxes)
        res['category_id'] = product.categ_id.id
        return res
