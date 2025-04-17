
from odoo import models, fields,api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    tag_ids = fields.Many2many('crm.tag', string='Sale Order Tags')

