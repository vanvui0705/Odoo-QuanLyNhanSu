# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class holiday_allowance(models.Model):
    _name = "holiday.allowance"

    _description = ""

    employee = fields.Many2one('hr.employee', 'name', Required=True)
    id_employee = fields.Char('ID Employee', required=True)
    assistant_holiday = fields.Many2many(comodel_name='assistant.holiday')
    assistant_dateoff = fields.One2many(comodel_name='assistant.dateoff',inverse_name='id')



class holiday_name(models.Model):
        _name = "holiday.name"
        _description = ""
        _order = 'name'

        name = fields.Char( required=True,string='Holiday name')


class support_type(models.Model):
        _name = "support.type"
        _description = ""
        _order = 'name'

        name = fields.Char( required=True, string='Support type')



class assistant_holiday(models.Model):
        _name = "assistant.holiday"
        _description = ""


        holiday_name = fields.Many2one('holiday.name', 'name',Required=True, delegate=True )
        date_from = fields.Date(
            'Start Date', required=True)
        date_to = fields.Date(
            'End Date', required=True)
        time_offset = fields.Date(
            'Time offset', required=True)
        assistant = fields.Integer('Assistant', default=500000)
        note = fields.Text('Note')
        Support_for_vacation_expenses = fields.Many2one('support.type', 'name', Required=True, delegate=True)

        id = fields.Char(string='ID', required=True, copy=False, readonly=True,
                         default=lambda seft: _('New'))

        @api.model
        def create(self, vals):
            if vals.get('id', ('New')) == ('New'):
                vals['id'] = self.env['ir.sequence'].next_by_code('assistant_holiday.id') or _('New')
            res = super(assistant_holiday, self).create(vals)
            return res





class assistant_dateoff(models.Model):
    _name = "assistant.dateoff"
    _description = ""

    total_number_of_holidays_per_year = fields.Integer('Total number of holidays per year', default=1)
    number_of_days_off = fields.Integer('Number of day off', default=1)
    remaining_eave_days = fields.Integer('Remaining leave days', default=1)
    assistant = fields.Integer('Assistant', default=500000)
    Support_for_vacation_expenses = fields.Selection([
        ('Train tickets', 'Train tickets'),
        ('Plane ticket', 'Plane ticket'),
        ('Bus ticket', 'Bus ticket')
    ], string='Support_Type', default='Train tickets')
    note = fields.Text('Reason')
    id = fields.Char(string='ID', required=True, copy=False, readonly=True,
                     default=lambda seft: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('id', ('New')) == ('New'):
            vals['id'] = self.env['ir.sequence'].next_by_code('assistant_dateoff.id') or _('New')
        res = super(assistant_dateoff, self).create(vals)
        return res




