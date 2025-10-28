from odoo import models, fields

class PatientTags(models.Model):
    _name = 'patient.tags'
    _description = 'Patient Tags'
    _order = 'sequence'

    name = fields.Char(string='Name')
    sequence = fields.Integer(string='Sequence', default=10)