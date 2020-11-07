from odoo import models, fields

class Stage(models.Model):
    _name = 'todo.task.stage'
    _description = 'Todo Task Stage'
    _order = 'sequence, name'
    # string fields
    name = fields.Char('Name', translate=True)
    desc = fields.Text('Description')
    state = fields.Selection([
        ('draft', 'New'),
        ('open', 'Started'),
        ('done', 'Closed')
    ], 'State')
    docs = fields.Html('Documentation')
    # numeric fields
    sequence = fields.Integer('Sequence')
    perc_complete = fields.Float('% Complete', (3, 2))
    # date fields
    date_effective = fields.Date('Effective Date')
    # other dields
    fold = fields.Boolean('Folded?')
    image = fields.Binary('Image')
    task_ids = fields.One2many('todo.task', 'stage_id', string='Tasks in this stage')