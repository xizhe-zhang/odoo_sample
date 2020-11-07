{
    'name': 'Add Stages and Tags to To-Dos',
    'description': 'Organize To-Do Tasks using Stages and Tags',
    'author': 'Ahmad M Ameen',
    'depends': ['todo_app', 'mail'],
    'application': False,
    'data': [
        'security/ir.model.access.csv',
        'views/todo_menu.xml',
        'views/todo_view.xml',
    ],
    'demo': [
        'data/todo.task.csv',
        'data/todo_task.xml',
    ]
}
