from odoo import http

class Todo(http.Controller):

    @http.route('/todo')
    def main(self):
        TodoTask = http.request.env['todo.task']
        domain_todo = [('is_done', '=', False)]
        tasks = TodoTask.search(domain_todo)
        context = {'tasks': tasks}
        return http.request.render('todo_app.index_template', context)