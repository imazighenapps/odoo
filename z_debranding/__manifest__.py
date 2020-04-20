{
    'name': "Backend debranding",
    'version': '12.0.1',
    'author': 'Imazighen',
    'license': 'LGPL-3',
    'category': 'Debranding',
    'images': ['images/web_debranding.png'],
    'support':'imazighenapps@gmail.com',
    'price': 24.00,
    'currency': 'EUR',
    'depends': [
        'web',
        'im_livechat',
        'mail',
    ],
    'data': [
        'data.xml',
        'views.xml',
        'js.xml',
        'pre_install.xml',
    ],
    'qweb': [
        'static/src/xml/web.xml',
    ],
    "post_load": 'post_load',
    'auto_install': False,
    'uninstall_hook': 'uninstall_hook',
    'installable': True,
}
