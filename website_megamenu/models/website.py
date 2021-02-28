from odoo import api, fields, models

class website(models.Model):
    _inherit = "website"

    # to render main parent product.public.category website specific
    def category_check(self):
        return self.env['product.public.category'].sudo().search([('website_published','=',True),('parent_id', '=', False),('website_id', 'in', (False,self.id))])
