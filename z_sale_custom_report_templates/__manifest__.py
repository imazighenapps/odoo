# -*- coding: utf-8 -*-
{
        'name': "Sale Custom Report Templates",
        'license': 'LGPL-3',
        'support': 'imazighenapps@gmail.com',

        'summary': """ """,

        'description': """
        """,

    'author': "Imazighen",
   
    'category': 'Sale & Templates Report',
    'images': ['static/description/icon.png'],

    'version': '13.1',
    'price': 15,
    'currency': 'EUR',
    # any module necessary for this one to work correctly
    'depends': ['base','z_base_custom_report_templates','sale'],
    'external_dependencies': {'python': ['num2words', 'PyPDF2']},

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        
        'views/report_style_views.xml',
        'reports/sale_order_reports.xml',

        'sale_order/order_lines.xml',
        'sale_order/order_lines_ascend.xml',
        'sale_order/switch_templates.xml',
        'sale_order/sale_order_view.xml',
        'sale_order/odoo_template.xml',
        'sale_order/retro_template.xml',
        'sale_order/classic_template.xml',
        'sale_order/tva_template.xml',
        'sale_order/band_template.xml',
        'sale_order/military_template.xml',
        'sale_order/western_template.xml',
        'sale_order/slim_template.xml',
        'sale_order/cubic_template.xml',
        'sale_order/clean_template.xml',
        'sale_order/modern_template.xml',
        'sale_order/100miles_template.xml',
        'sale_order/ascend_template.xml',

    ],
   
    'demo': [
            # 'demo.xml',
            ],
    'installable': True,
    'auto_install': False,
    'application': True,

}
