# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class medical_program(models.Model):
    _name = "medical.program"

    _description = ""

    employee = fields.Many2one('hr.employee', 'name', Required=True)
    id_employee = fields.Char('ID Employee', required=True)
    code_health = fields.Char('Code Health insurance', required=True)
    Date_created = fields.Date('Date created', required=False)
    Date_finish = fields.Date('Date finish', required=False)
    PHE = fields.Selection([
        ('part 1', 'part 1'),
        ('part 2', 'part 2')
    ], string='Periodic health examination', default='part 1')
    medical_examination_program_participated = fields.Many2many(comodel_name='program.participated')
    medical_history= fields.One2many(comodel_name='medical.history',inverse_name='id')

    id = fields.Char(string='ID', required=True, copy=False, readonly=True,
                         default=lambda seft: _('New'))
    @api.model
    def create(self, vals):
        if vals.get('id', ('New')) == ('New'):
            vals['id'] = self.env['ir.sequence'].next_by_code('classlist.id') or _('New')
        res = super(medical_program, self).create(vals)
        return res

    @api.constrains('Date_finish')
    def onchange_end_dates(self):
        if (self.Date_created and self.Date_finish) and (self.Date_created < self.Date_finish):
            raise ValueError(('Time end must be greater than or equal to Time start.'))



class program_participated(models.Model):
    _name = "program.participated"

    id = fields.Char(string='ID', required=True, copy=False, readonly=True,
                         default=lambda seft: _('New'))
    @api.model
    def create(self, vals):
        if vals.get('id', ('New')) == ('New'):
            vals['id'] = self.env['ir.sequence'].next_by_code('classlist.id') or _('New')
        res = super(program_participated, self).create(vals)
        return res
    Date = fields.Date('Time', required=False)
    Location = fields.Text(' Location')
    program_name = fields.Text(' Program name')
    service_fee = fields.Float('Service fee', required=True)




class medical_history(models.Model):
    _name = "medical.history"

    id = fields.Char(string='ID', required=True, copy=False, readonly=True,
                         default=lambda seft: _('New'))
    @api.model
    def create(self, vals):
        if vals.get('id', ('New')) == ('New'):
            vals['id'] = self.env['ir.sequence'].next_by_code('medical_history.id') or _('New')
        res = super(medical_history, self).create(vals)
        return res
    Date = fields.Date('Time', required=False)
    Location = fields.Text(' Location')
    Content = fields.Text(' Content')















