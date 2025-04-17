from odoo import models, api
from odoo.exceptions import ValidationError

class ProductCategory(models.Model):
    _inherit = 'product.category'

   
    @api.model
    def create(self, vals):
        if 'name' in vals:
            existing_category = self.search([('name', '=', vals['name'])])
            if existing_category:
                raise ValidationError('Category name must be unique.')
        return super(ProductCategory, self).create(vals)

    def write(self, vals):
        if 'name' in vals:
            existing_category = self.search([('name', '=', vals['name'])])
            if existing_category:
                raise ValidationError('Category name must be unique.')
        return super(ProductCategory, self).write(vals)
