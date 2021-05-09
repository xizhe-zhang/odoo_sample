from odoo import models, fields, api

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-do Task'
    
    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('active?', default=True)
    user_id = fields.Many2one('res.users', string='Responsible', default=lambda self: self.env.user)
    team_ids = fields.Many2many('res.partner', string='Team')
    date_deadline = fields.Date(string='Deadline')

    def do_clear_done(self):
        for task in self:
            task.active = False
        return True

    def write(self, values):
        if 'active' not in values:
            values['active'] = True
        super().write(values)
