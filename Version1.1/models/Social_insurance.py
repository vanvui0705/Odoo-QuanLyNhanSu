# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class social_insurance(models.Model):
    _name = "social.insurance"

    _description = ""

    employee = fields.Char('Employee', required=True)
    code_BHXH = fields.Char('ID Social insurance', required=True)
    code_BHYT = fields.Char('ID Health insurance',required=True)
    Date_created = fields.Date('Date created', required=False)
    Date_finish = fields.Date('Date finish', required=False)
    amount_of_money = fields.Float('Amount of money',required=True)
    detail = fields.One2many(string='Detail insurance',comodel_name='detail.insurance', inverse_name="id")




class detail_insurance(models.Model):
    _name = "detail.insurance"
    _description = ""


    from_month = fields.Date('From month', required=False)
    to_month = fields.Date('To month', required=False)
    Basic_wage_rates = fields.Float('Basic wage ratesy ', required=True)
    payment_rate = fields.Integer('Payment rate(%)', default=7)





