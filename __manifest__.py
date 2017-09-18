# -*- coding: utf-8 -*-
{
    'name'     : 'InfoSaône - Module Odoo pour SNTBG',
    'version'  : '0.1',
    'author'   : 'InfoSaône',
    'category' : 'InfoSaône/SNTBG',


    'description': """
InfoSaône - Module Odoo pour SNTBG
===================================================
""",
    'maintainer' : 'InfoSaône',
    'website'    : 'http://www.infosaone.com',
    'depends'    : [
        'base',
        'stock',
        'sale',
        'mail',
        'account',
        'account_accountant',
        'purchase',
        'document',
],
    'data' : [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/report_invoice.xml',
        'views/sale_view.xml',
        'views/is_immatriculation_view.xml',
        'views/product_view.xml',
        'views/account_invoice_view.xml',
        'views/is_export_compta_view.xml',
        'views/partner_view.xml',
    ],
    'installable': True,
    'application': True,
    'qweb': [
    ],
}

