from odoo import models, fields

class Tag(models.Model):
    _name = 'todo.task.tag'
    _description = 'Todo Task Tag'
    
    name = fields.Char('Name', translate=True)
    task_ids = fields.Many2many('todo.task', string='Tasks')