# -*- coding: utf-8 -*-
{
        'name': "Invoice Custom Report Templates",
        'license': 'LGPL-3',
        'support': 'imazighenapps@gmail.com',

        'summary': """Invoice Custom Report Templates Designing """,

        'description': """Invoice Custom Report Templates Designing...
        """,

    'author': "Imazighen",
   
    'category': 'Account & Templates Report',
    'images': ['static/description/icon.png'],

    'version': '13.1',
    'price': 15,
    'currency': 'EUR',
    # any module necessary for this one to work correctly
    'depends': ['base','z_base_custom_report_templates','account'],
    'external_dependencies': {'python': ['num2words', 'PyPDF2']},

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        
        'views/report_style_views.xml',
        'reports/invoice_reports.xml',

        'invoice/invoice_lines.xml',
        'invoice/ascend_invoice_lines.xml',
        'invoice/switch_templates.xml',
        'invoice/dl_envelope.xml',
        'invoice/modern_template.xml',
        'invoice/classic_template.xml',
        'invoice/retro_template.xml',
        'invoice/tva_template.xml',
        'invoice/odoo_template.xml',
        'invoice/band_template.xml',
        'invoice/military_template.xml',
        'invoice/western_template.xml',
        'invoice/slim_template.xml',
        'invoice/cubic_template.xml',
        'invoice/clean_template.xml',
        'invoice/100miles_template.xml',
        'invoice/ascend_template.xml',
        'invoice/account_invoice_view.xml',


    ],
   
    'demo': [
            # 'demo.xml',
            ],
    'installable': True,
    'auto_install': False,
    'application': True,

}
