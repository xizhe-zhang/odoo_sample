{
    'name': 'To-Do Application',
    'description': 'Manage personal to-do tasks.',
    'author': 'Ahmad M Ameen',
    'depends': ['base'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'security/todo_access_rule.xml',
        'views/todo_menu.xml',
        'views/todo_view.xml',
        'views/res_partner_view.xml',
        'views/index_template.xml',
    ],
    'demo': [],
}



