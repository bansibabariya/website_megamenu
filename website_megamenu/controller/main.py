import odoo
from odoo import http, fields, tools, _
from odoo.http import request


class menuHtmlBuilder(http.Controller):

    # Redirect on the website for menu editor purpose from the back-end
    @http.route('/menu_html_builder', type='http', auth="user", website=True)
    def website_menu(self, model=False, id=False, **kw):
        if id and model:
            id = int(id)
            record = request.env[model].browse(id)
            values = {
                'record': record,
                'model': model,
                'id': id,
            }
            return request.render("website_megamenu.website_menu_edit", values)

