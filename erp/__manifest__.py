# -*- coding: utf-8 -*-customer
{
    'name': "HR NHOM10",
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
        'views/kpi.xml',
        'views/menu.xml',
        'report/kpi_report_employee.xml',
        'report/report_kpi.xml',


    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}