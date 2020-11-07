from odoo import models, fields, api
from odoo import exceptions

class Patient(models.Model):
    _name = 'patient.health'
    _description = 'Patient Record'

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    age = fields.Integer(string='Age')
    date_birth = fields.Date(string='Date of Birth')
    gender = fields.Selection([('Male', 'Male'), ('Female', 'Female')])
    address = fields.Text(string='Home Address')
