# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Ajuste(models.Model):

    _inherit = 'stock.inventory.line'

    account_ids = fields.Many2one(
        comodel_name='account.analytic.account',
        string="Analytic Account",
    )

    price = fields.Float(
        related='product_id.list_price',
        store=True,
    )

    descuento = fields.Float(
        compute="_descuento",
        store=True,
    )
    description = fields.Char(
        string="Description",
        store=True,
    )

    @api.depends('product_qty')
    def _descuento(self):
        for record in self:
            record.descuento = (record.price * record.product_qty) * -1

    @api.constrains('product_id.name')
    def _account_analytic(self):
        for record in self:
            record.account_analytic = self.env['account.analytic.line'].search([
                ('date', '=', self.inventory_date),
                ('name', '=', self.product_id.name),
                ('account_id', '=', self.account_ids.id),
                ('motivo', '=', self.description),
                ('amount', '=', self.descuento),
            ])
            if record.account_analytic:
                raise ValidationError(_("Los registros ya existen"))

            elif not record.account_analytic:
                self.env['account.analytic.line'].create({
                    'date': self.inventory_date,
                    'name': self.product_id.name,
                    'account_id': self.account_ids.id,
                    'motivo': self.description,
                    'amount': self.descuento,
                })

