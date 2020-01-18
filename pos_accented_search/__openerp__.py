# -*- coding: utf-8 -*-
{
    'name': "pos_accented_search",

    'summary': """
        Makes tjhe POS product search insensitive to accented characters.""",

    'description': """
        This add-on make pos product search insensitive to accented characters in the product
        name. For instance, café will match both cafe and café.  
    """,

    'author': "Le Nid",
    'website': "http://www.lenid.ch",
    'license': 'AGPL-3',
    'category': 'Point of Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        'views/templates.xml',
    ],
}