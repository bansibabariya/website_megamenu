from odoo import api, fields, models
from odoo.tools.translate import html_translate

class website_menu(models.Model):
    _inherit = "website.menu"
    
    html_menu = fields.Html('Menu Design Block',translate=html_translate)
    is_dynamic_menu = fields.Boolean("Is Dynamic Menu",default=False)

    # method whcih redirect to frontend for design menu html structure
    def action_edit_menu(self, context=None):
        if not len(self.ids) == 1:
            raise ValueError('One and only one ID allowed for this action')

        url = '/menu_html_builder?model=website.menu&id=%d&enable_editor=1' % (self.id)
        return {
            'name': ('Edit Template'),
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'self',
        }