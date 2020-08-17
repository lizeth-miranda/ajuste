# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import api, fields, models


class Cuenta(models.Model):
    _inherit = 'account.analytic.line'

    motivo = fields.Char(
        String="Motivo",
        store=True,
    )
