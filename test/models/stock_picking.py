
from odoo import models, fields

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    tag_ids = fields.Many2many('crm.tag', string='Sale Order Tags')
