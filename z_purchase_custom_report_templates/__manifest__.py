# -*- coding: utf-8 -*-
{
        'name': "Purchase Custom Report Templates",
        'license': 'LGPL-3',
        'support': 'imazighenapps@gmail.com',

        'summary': """Purchase Custom Report Templates Designing """,

        'description': """Purchase Custom Report Templates Designing...
        """,

    'author': "Imazighen",
   
    'category': 'Purchase & Templates Report',
    'images': ['static/description/icon.png'],

    'version': '13.1',
    'price': 15,
    'currency': 'EUR',
    # any module necessary for this one to work correctly
    'depends': ['base','z_base_custom_report_templates','purchase'],
    'external_dependencies': {'python': ['num2words', 'PyPDF2']},

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        
        'views/report_style_views.xml',
        'reports/purchase_order_reports.xml',
        'reports/rfq_reports.xml',

        'purchase_order/purchase_lines.xml',
        'purchase_order/purchase_lines_ascend.xml',
        'purchase_order/switch_templates.xml',
        'purchase_order/purchase_order_view.xml',
        'purchase_order/odoo_template.xml',
        'purchase_order/retro_template.xml',
        'purchase_order/classic_template.xml',
        'purchase_order/tva_template.xml',
        'purchase_order/modern_template.xml',
        'purchase_order/band_template.xml',
        'purchase_order/military_template.xml',
        'purchase_order/western_template.xml',
        'purchase_order/slim_template.xml',
        'purchase_order/cubic_template.xml',
        'purchase_order/clean_template.xml',
        'purchase_order/ascend_template.xml',

        'rfq/rfq_lines.xml',
        'rfq/rfq_lines_ascend.xml',
        'rfq/switch_templates.xml',
        'rfq/rfq_view.xml',
        'rfq/odoo_template.xml',
        'rfq/retro_template.xml',
        'rfq/classic_template.xml',
        'rfq/tva_template.xml',
        'rfq/modern_template.xml',
        'rfq/band_template.xml',
        'rfq/military_template.xml',
        'rfq/western_template.xml',
        'rfq/slim_template.xml',
        'rfq/cubic_template.xml',
        'rfq/clean_template.xml',
        'rfq/ascend_template.xml',

    ],
   
    'demo': [
            # 'demo.xml',
            ],
    'installable': True,
    'auto_install': False,
    'application': True,

}
