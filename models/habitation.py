# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class Habitation(models.Model):

    _name = 'partner_contact_habitation.habitation'
    _description = 'Form of habitation'

    name = fields.Char('Name', required=True, translate=True)
