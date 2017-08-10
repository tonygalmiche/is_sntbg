# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_lavage = fields.Boolean('Lavage', default=False, help="Article utilisé pour les lavages")



