# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.exceptions import UserError
from odoo.tools.safe_eval import safe_eval


class TemplateSettings(models.Model):
    _inherit = "report.template.settings"
    _description = "Report Style Settings"


    @api.model
    def _default_rfq_template(self):
        def_tpl = self.env['ir.ui.view'].search(
            [('key', 'like', 'z_purchase_custom_report_templates.RFQ\_%\_document'),
             ('type', '=', 'qweb')],
            order='key asc',
            limit=1)
        return def_tpl or self.env.ref(
            'purchase.report_purchasequotation_document')

    @api.model
    def _default_po_template(self):
        def_tpl = self.env['ir.ui.view'].search(
            [('key', 'like', 'z_purchase_custom_report_templates.PO\_%\_document'),
             ('type', '=', 'qweb')],
            order='key asc',
            limit=1)
        return def_tpl or self.env.ref(
            'purchase.report_purchaseorder_document')

   
    template_po = fields.Many2one(
        'ir.ui.view',
        'Purchase Order Template',
        default=_default_po_template,
        domain=
        "[('type', '=', 'qweb'), ('key', 'like', 'z_purchase_custom_report_templates.PO\_%\_document' )]",
        required=False)

    template_rfq = fields.Many2one(
        'ir.ui.view',
        'RFQ Template',
        default=_default_rfq_template,
        domain=
        "[('type', '=', 'qweb'), ('key', 'like', 'z_purchase_custom_report_templates.RFQ\_%\_document' )]",
        required=False)


    
  
