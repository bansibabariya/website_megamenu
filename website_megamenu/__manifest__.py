# Copyright 2021 Odoo Helper
# See LICENSE file for full copyright and licensing details.
#
##############################################################################
{
    'name': 'Website Megamenu',
    'category': 'website',
    'version': '12.0.1',

    'summary': 'This Module provide megamenu with different style and also phone view responsive',

    'description': """
    This Module provide megamenu with different style and also phone view responsive
        """,

    'author': 'Odoo Helper',
    'license': 'AGPL-3',

    'depends': ['base', 'website', 'portal', 'website_sale'],
    'data': [
        'views/website_menu_view.xml',
        'views/assets.xml',
        'views/template.xml',
        'views/custom_snippets.xml',
        'views/menu_config.xml',
    ],

    'images': ['images/OdooHelper.png'],

    'price': 28.56,
    'currency': 'USD',

    'installable': True,
    'application': False
}
