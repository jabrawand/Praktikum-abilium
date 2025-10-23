
from odoo import models, fields, api


class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Real Estate Property Type'
    _order = 'name'

    name = fields.Char(string="Property Type", required=True)
    property_ids = fields.One2many(
        'estate.property',
        'property_type',
        string='Properties'
    )

    sequence = fields.Integer(string='Sequence', default=1, help='Used to order the property types')
    

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'A property type name must be unique'),
    ]

    

