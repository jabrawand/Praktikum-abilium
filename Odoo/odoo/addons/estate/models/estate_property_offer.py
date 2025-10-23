from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError
from odoo.tools.float_utils import float_is_zero, float_compare

import logging

_logger = logging.getLogger(__name__)


class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offer'
    _order = 'price desc'
    
    
    price = fields.Float(string='Price')
    status = fields.Selection(
      string="Status",
      selection=[
        ('accepted', 'Accepted'),
        ('refused', 'Refused')
      ],
      default=None
    )
    partner_id = fields.Many2one('res.partner', string="Partner", required=True)
    property_id = fields.Many2one('estate.property', string="Property",  required=True)
    validity = fields.Integer(string="Validity (days)", default=7)
    date_deadline = fields.Date(compute='_compute_date_deadline', inverse='_inverse_date_deadline', store=True, search='_search_date_deadline')

    # Deadline berechnen
    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
      for record in self:
        # Wenn bereits ein create_date-Eintrag besteht
        if record.create_date:
          record.date_deadline = record.create_date + timedelta(days=record.validity)
        # Wenn ein neuer Datensatz eingetragen wird  
        else:
          record.date_deadline = datetime.now().date() + timedelta(days=record.validity)

    def _inverse_date_deadline(self):
      for record in self:
        if record.date_deadline and record.create_date:
          record.validity = (record.date_deadline - record.create_date.date()).days
        else:
          record.validity = 7 #Fallback

    def action_accept(self):
      self.ensure_one()
      self.status = 'accepted'
      self.property_id.action_accept_offer()
      

    def action_refuse(self):
      self.ensure_one()
      self.status = 'refused'

    @api.depends('partner_id.name', 'date_deadline')
    def _compute_display_name(self):
      for record in self:
        record.display_name = "%s - %s" % (record.partner_id.name, record.date_deadline)

    @api.model
    def create(self, vals):
      record = super(EstatePropertyOffer, self).create(vals)
      if record.property_id:
        record.property_id.action_offer_recieved()
      return record