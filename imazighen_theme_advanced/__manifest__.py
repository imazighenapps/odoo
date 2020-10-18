# -*- coding: utf-8 -*-

{
    'name': 'Imazighen Advanced Enterprise Backend Theme',
    'category': 'Themes/Backend',
    'version': '13.2',
    'summary': """ Advanced Odoo Enterprise Backend Theme For Community Edition""",
    'description':
        """
Advanced Theme Enterprise Web Client.
===========================

This module modifies the web addon to provide Enterprise design and responsiveness.
        """,
    "author": "Imazighen",
    "price": "40",
    "currency": "EUR",
    "support": "imazighenapps@gmail.com",
    'depends': ['web','imazighen_theme'],
    'auto_install': False,
    'data': [
        'views/webclient_templates.xml',
        'views/res_config_settings_views.xml',
        'views/web_widget_colorpicker_view.xml',
      
    ],
   "images": [
        'static/description/panelz.png',
      
    ],
    'qweb': [
       
          "static/src/xml/*.xml",
    ],
     "license": "OPL-1",
}
