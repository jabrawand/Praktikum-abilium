from odoo import models, fields, api

class KnifeColors(models.Model):
    _name = 'vx.knife.colors'
    _description = 'All colors of Victorinox knives'

    name = fields.Char(string='Color Name')