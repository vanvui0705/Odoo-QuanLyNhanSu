# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class medical_program(models.Model):
    _name = "medical.program"

    _description = ""

    employee = fields.Char('Employee', required=True)
    code_health = fields.Char('Code Health insurance', required=True)
    Date_created = fields.Date('Date created', required=False)
    PHE = fields.Selection([
        ('part 1', 'part 1'),
        ('part 2', 'part 2')
    ], string='Periodic health examination', default='part 1')
    medical_examination_program_participated = fields.Text(' Medical examination program participated')
    medical_history= fields.One2many(comodel_name='medical.history', inverse_name='id')

    id = fields.Char(string='ID', required=True, copy=False, readonly=True,
                         default=lambda seft: _('New'))
    @api.model
    def create(self, vals):
        if vals.get('id', ('New')) == ('New'):
            vals['id'] = self.env['ir.sequence'].next_by_code('classlist.id') or _('New')
        res = super(medical_program, self).create(vals)
        return res



class medical_history(models.Model):
    _name = "medical.history"

    medical_history_id = fields.Char('Id', default=1)
    Date = fields.Date('Time', required=False)
    Location = fields.Text(' Location')
    Content = fields.Text(' Content')













