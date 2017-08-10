# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    is_date_intervention = fields.Date(string='Date intervention', required=True, index=True, copy=False, default=fields.Datetime.now)


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    is_immat1 = fields.Many2one('is.immatriculation', string='Tracteur'     , help='Immatriculation du tracteur')
    is_immat2 = fields.Many2one('is.immatriculation', string='Semi-Remorque', help='Immatriculation du semi-remorque')
