from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Knives(models.Model):
    _name = 'vx.knives'
    _description = 'Victorinox Knives'

    # Fields
    article_number = fields.Char(string='Article Number')
    name = fields.Char(string='Name')
    color_ids = fields.Many2many(
        'vx.knife.colors', 
        'knives_colors_rel', 
        'knive_id', 
        'color_id',
        string='Color')
    description = fields.Text(string='Description')

    # SQL Constrants
    _sql_constraints = [
        
        ('check_unique_article_number', 'UNIQUE(aritcle_number)', 'The articel number must be unique')
    ]

    # Methode zur Überprüfung der Artikelnummerlänge
    @api.constrains('article_number')
    def _check_article_number_length(self):
        for record in self:
            if len(record.article_number) < 4:
                raise ValidationError('The article number must contain at least 4 characters.')

   