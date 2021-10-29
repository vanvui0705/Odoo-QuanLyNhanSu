# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class social_insurance(models.Model):
    _name = "social.insurance"

    _description = ""


    employee = fields.Many2one('hr.employee', 'name', Required=True)
    id_employee = fields.Char('ID Employee', required=True)
    code_BHXH = fields.Char('ID Social insurance', required=True)
    code_BHYT = fields.Char('ID Health insurance',required=True)
    Date_created = fields.Date('Date created', required=False)
    Date_finish = fields.Date('Date finish', required=False)
    # amount_of_money = fields.Float('Amount of money',required=True)
    # detail = fields.One2many(string='Detail insurance', comodel_name='detail.insurance', inverse_name="id")
    detail = fields.One2many('detail.insurance','id')
    Job_Positions = fields.Many2one(comodel_name='hr.job', delegate=True)
    id = fields.Char(string='ID', required=True, copy=False, readonly=True,
                     default=lambda seft: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('id', ('New')) == ('New'):
            vals['id'] = self.env['ir.sequence'].next_by_code('social_insurance.id') or _('New')
        res = super(social_insurance, self).create(vals)
        return res
    _sql_constraints = [
        ('id_employee','unique (id_employee)', 'Customer already exists ! create failed')
    ]

class detail_insurance(models.Model):
    _name = "detail.insurance"
    _description = ""


    from_month = fields.Date('From month', required=False)
    to_month = fields.Date('To month', required=False)
    Basic_wage_rates = fields.Float('Basic wage ratesy ', required=True)
    payment_rate = fields.Integer('Payment rate(%)', default=7)
    amount_of_money = fields.Float('Amount of money',required=True)

    id = fields.Char(string='ID', required=True, copy=False, readonly=True,
                     default=lambda seft: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('id', ('New')) == ('New'):
            vals['id'] = self.env['ir.sequence'].next_by_code('detail_insurance.id') or _('New')
        res = super(detail_insurance, self).create(vals)
        return res




