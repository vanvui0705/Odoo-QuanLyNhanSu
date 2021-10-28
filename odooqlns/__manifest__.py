# -*- coding: utf-8 -*-customer
{
    'name': "HR 10",
    'summary': """employee manager """,
    'description': """Managing employee information""",
    'author': "nhi",
    'website': "",
    'category': 'Uncategorized',
    'sequence': -100,
    'version': '0.1',
    'depends': [
        'hr',
    ],
    'data': [

        'views/templates.xml',
        'views/views.xml',
        'views/medical_program.xml',
        'views/employee.xml',
        'views/hr.xml',
        'views/business.xml',
        'views/production.xml',
        'views/finance.xml',

    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}