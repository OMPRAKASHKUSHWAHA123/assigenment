from odoo import models, api,fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    display_name = fields.Char(compute='_compute_display_name', store=True)

    @api.depends('name', 'ref')
    def _compute_display_name(self):
        for rec in self:
            if rec.ref:
                rec.display_name = f"{rec.name} [{rec.ref}]"
            else:
                rec.display_name = rec.name

  
    

    
