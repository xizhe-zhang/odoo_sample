from odoo import models, fields, api
from odoo import exceptions
import logging

_logger = logging.getLogger(__name__)

class TodoWizard(models.TransientModel):
    _name = 'todo.wizard'
    _description = 'To-do Mass Assignment'

    task_ids = fields.Many2many('todo.task', string='Tasks')
    new_deadline = fields.Date('Set Deadline')
    new_user_id = fields.Many2many('res.users', string='Set Responsible')

    @api.model
    def default_get(self, field_names):
        defaults = super(TodoWizard, self).default_get(field_names)
        defaults['task_ids'] = self.env.context['active_ids']
        return defaults
        
    @api.multi
    def do_mass_update(self):
        self.ensure_one()
        if not (self.new_deadline or self.new_user_id):
            raise exceptions.ValidationError('No data to update!')
        # Logging debug messages
        _logger.debug('Mass update on Todo Tasks %s', self.task_ids.ids)
        vals = {}
        if self.new_deadline:
            vals['data_deadline'] = self.new_deadline
        if self.new_user_id:
            val['user_id'] = self.new_user_id
        if vals:
            self.task_ids.write(vals)
        return True

    @api.multi
    def do_count_tasks(self):
        Task = self.env['todo.task']
        count = Task.search_count([('is_done', '=', False)])
        raise exceptions.Warning('There are %d active tasks.' %count)
        return True
        
    @api.multi
    def _reopen_form(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new'
        }

    @api.multi
    def do_populate_tasks(self):
        self.ensure_one()
        Task = self.env['todo.task']
        all_task = Task.search([('is_done', '=', False)])
        self.task_ids = all_task
        return self._reopen_form
