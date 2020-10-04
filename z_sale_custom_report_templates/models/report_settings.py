# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.exceptions import UserError
from odoo.tools.safe_eval import safe_eval


class TemplateSettings(models.Model):
    _inherit = "report.template.settings"
    _description = "Report Style Settings"

    @api.model
    def _default_so_template(self):
        def_tpl = self.env['ir.ui.view'].search(
            [('key', 'like', 'z_sale_custom_report_templates.SO\_%\_document'),
             ('type', '=', 'qweb')],
            order='key asc',
            limit=1)
        return def_tpl or self.env.ref('sale.report_saleorder_document')

   
    template_so = fields.Many2one(
        'ir.ui.view',
        'Order/Quote Template',
        default=_default_so_template,
        domain=
        "[('type', '=', 'qweb'), ('key', 'like', 'z_sale_custom_report_templates.SO\_%\_document' )]",
        required=False)

    
  
