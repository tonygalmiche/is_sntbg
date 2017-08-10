# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class IsImmatriculation(models.Model):
    _name = "is.immatriculation"
    _sql_constraints = [('name_uniq','UNIQUE(name)', u'Ce code existe déjà')]

    name        = fields.Char(string='Immatriculation', required=True, index=True)
    commentaire = fields.Text(string='Commentaire')



