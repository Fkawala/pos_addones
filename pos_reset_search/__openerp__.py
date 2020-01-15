# -*- coding: utf-8 -*-
{
    'name': "pos_reset_search",

    'summary': """
        Reset search after click on product.""",

    'description': """
        The POS search workflow is to type in product until there is only on product left
        to be selected. Then the user will select the product by typing on enter. This 
        workflow is very efficient yet it requires user formation.
        
        This add-on modifies the POS search workflow. This add-on will enable the use to
        use the search to simply narrow down the product selection to a handfull of products. 
        The user can then either use the default workflow described above, or use the mouse to
        click on the product to add to the order.

        This new workflow is deemed less efficient but has proven to help beginers. 
    """,

    'author': 'Cooperative le Nid',
    'website': "http://www.lenid.ch",
    'license': 'AGPL-3',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Point of Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        'views/templates.xml',
    ],
}
