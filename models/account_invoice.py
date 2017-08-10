# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class AccountInvoice(models.Model):
    _inherit = "account.invoice"


    @api.depends('invoice_line_ids')
    def _compute(self):
        for obj in self:
            nb=0
            for line in obj.invoice_line_ids:
                if line.product_id.is_lavage:
                    nb=nb+line.quantity
            obj.is_nb_lavages=nb


    is_nb_lavages = fields.Char('Nombre de lavages', compute='_compute', store=False, readonly=True)



class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    _order = "invoice_id,id desc"

