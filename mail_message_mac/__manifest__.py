# -*- coding: utf-8 -*-
{
    'name': "Messages with Mac Address",
    'summary': """
        Add new features in Chatter""",
    'description': """
        Add new features in Chatter to display mac address along with name of author.
    """,

    'author': "Silverdaletech",
    'website': "http://www.silverdaletech.com",
    'category': 'Message',
    'version': '15.0',
    'sequence': 2,
    'depends': ['base', 'web', 'mail'],

    'data': [
        'views/mail_message.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'mail_message_mac/static/src/js/message.js',

        ],
        'web.assets_qweb': [
            'mail_message_mac/static/src/xml/message.xml',
        ],
    },
    "installable": True,
    "auto_install": False,
    'application': True,
}
