from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = 'todo.task'
    _inherit = ['todo.task', 'mail.thread']
    _sql_constraints = [('todo_task_name_unique', 'UNIQUE (name, active)', 'Task title must be unique')]

    name = fields.Char(help="What need to be done?")
    effort_estimate = fields.Integer()
    stage_id = fields.Many2one("todo.task.stage", string="Stage", relation='todo_task_stage_rel')
    tag_ids = fields.Many2many("todo.task.tag", string="Tags", relation='todo_task_tag_rel', auto_join=False, context={}, domain=[], ondelete='cascade')
    stage_fold = fields.Boolean('Stage Folded?', compute='_compute_stage_fold', store=True, inverse='_write_stage_fold', search='_search_stage_fold')
    state = fields.Selection(related='stage_id.state', string='Stage State', store=True)
    #thread_id = fields.Many2one('mail.thread')

    @api.depends('stage_id.fold')
    def _compute_stage_fold(self):
        for todo in self:
            todo.stage_fold = todo.stage_id.fold
        return True

    def _write_stage_fold(self):
        for todo in self:
            todo.stage_id.fold = todo.stage_fold
        return True

    def _search_stage_fold(self, operator, value):
        return [('stage_id.fold', operator, value)]

    @api.constrains('name')
    def _check_name_size(self):
        for todo in self:
            if len(todo.name) < 5:
                raise ValidationError('Must have 5 chars!')
        return True

    @api.onchange('user_id')
    def onchange_user_id(self):
        if not self.user_id:
            self.team_ids == None
            return {
                'warning':{
                    'title': 'No Responsible',
                    'message': 'Team was also reset'
                }
            }