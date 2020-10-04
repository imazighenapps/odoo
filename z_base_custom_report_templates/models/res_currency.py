# -*- coding: utf-8 -*-

from odoo import fields, models


class ResCurrency(models.Model):
    _inherit = "res.currency"


    currency_name = fields.Char('Currency Name',help="Currency full name e.g US Dollars")
