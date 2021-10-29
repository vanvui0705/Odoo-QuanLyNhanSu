# -*- coding: utf-8 -*-customer
{
    'name': "HR 10",
    'summary': """ """,
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

        # 'views/templates.xml',
        # 'views/views.xml',
        'views/medical_program.xml',
        'views/employee.xml',
        'views/Social_insurance.xml',
        'views/code.xml',
        'views/medical_history.xml',
        'views/holiday_allowance.xml',
        'views/business_keypi.xml',
        'views/hr_keypi.xml',
        'views/production_keypi.xml',
        'views/finance_keypi.xml',
        'views/menu.xml',

    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}