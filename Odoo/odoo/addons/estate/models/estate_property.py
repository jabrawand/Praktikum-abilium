from odoo import fields, models, api, _

class estate_property(models.Model):
    _name = "estate_property"
    _description = "estate property"

    name = fields.Char()