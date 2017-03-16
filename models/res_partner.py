# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class ResPartner(models.Model):

    _inherit = 'res.partner'

    habitation_id = fields.Many2one('partner_contact_habitation.habitation', 'Form of Habitation')
