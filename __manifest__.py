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
        'views/report_invoice.xml',
    ],
    'installable': True,
    'application': True,
    'qweb': [
    ],
}

