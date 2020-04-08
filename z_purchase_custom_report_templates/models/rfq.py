# -*- coding: utf-8 -*-

from odoo import fields, models


class RFQ(models.Model):
    """ @inherit purchase @model to add fields for report module"""
    _inherit = ["purchase.order"]

    rfq_style = fields.Many2one(
        'report.template.settings',
        'RFQ Style',
        help="Select style to use when printing the RFQ",
        default=lambda self: self.partner_id.style or self.env.user.company_id.
        df_style)
