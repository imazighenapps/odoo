# -*- coding: utf-8 -*-
{
        'name': "Base Custom Report Templates",
        'license': 'LGPL-3',
        'support': 'imazighenapps@gmail.com',

        'summary': """ Base Custom Report Templates Designing""",

        'description': """Base Custom Report Templates Designing...
        """,

    'author': "Imazighen",
 

    'category': 'Reports',
    'images': ['static/description/icon.png'],

    'version': '13.1',
    'price': 20,
    'currency': 'EUR',
    # any module necessary for this one to work correctly
    'depends': ['base','sale'],
    'external_dependencies': {'python': ['num2words', 'PyPDF2']},

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/res_company_view.xml',
        'views/res_config_view.xml',
        'views/res_currency.xml',
        'views/res_partner.xml',
        'views/company_footer.xml',
        'views/company_address.xml',
        'views/company_address_noname.xml',
        'views/category.xml',
        'views/report_style_views.xml',
        'views/ir_actions_report_xml.xml',
        'views/web_widget_colorpicker_view.xml',
    
        'data/res_currency_data.xml',
        'data/default_style.xml',
    ],
   
    'demo': [
            # 'demo.xml',
            ],
    'installable': True,
    'auto_install': False,
    'application': True,

}
