# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import api, fields, models, _
#from odoo.exceptions import ValidationError


class Fleet(models.Model):

    _inherit = 'fleet.vehicle.assignation.log'

    driver_id = fields.Many2one(
        required=False,
        readonly=True,
    )
    employee = fields.Many2one(
        comodel_name='hr.employee',
        string="Conductor",
    )
