# -*- coding: utf-8 -*-
{
    'name': "pos_accented_search",

    'summary': """
        Make POS product search insensitive to accented characters.""",

    'description': """
        make pos product search insensitive to accented characters in the product
        name. For instance, to search œuf will match oeuf and œuf, café will match
        cafe and café.  
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