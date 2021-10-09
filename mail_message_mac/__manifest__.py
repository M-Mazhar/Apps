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
    'version': '14.0',
    'sequence': 2,
    'depends': ['base', 'web', 'mail'],

    'data': [
        'views/assets.xml',
        'views/mail_message.xml',
    ],

    'qweb': [
        "static/src/xml/message.xml",
    ],
    "installable": True,
    "auto_install": False,
    'application': True,
}
