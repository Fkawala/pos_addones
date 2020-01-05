# -*- coding: utf-8 -*-
{
    'name': "pos_reset_search",

    'summary': """
        Reset search after click on product.""",

    'description': """
        Reset search after click on product when there are still multiple products
        in selection.
    """,

    'author': "Le Nid",
    'website': "http://www.lenid.ch",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Point of Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}