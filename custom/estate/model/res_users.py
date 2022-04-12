from odoo import models, fields


class EstateSalesPerson(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many('estate.property', 'sales_person_id', string='Property List')
