from odoo import models, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        if name:
            partners = self.search(['|', ('name', operator, name), ('ref', operator, name)] + args, limit=limit)
        else:
            partners = self.search(args, limit=limit)
        return partners.name_get()

    def name_get(self):
        result = []
        for partner in self:
            name = partner.name
            if partner.ref:
                name += f" [{partner.ref}]"
            result.append((partner.id, name))
        return result
    

    
