# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hr_keypi(models.Model):
    _name = "hr.keypi"
    _description = "HR Management"

    # Employee = fields.One2many('hr.employee', 'employee_ids')
    employee = fields.Many2one('hr.employee', 'name', Required=True)
    id = fields.Integer("ID", default='1')
    date = fields.Datetime("Time of creation", required=False)
    time_start = fields.Date("Evaluation start time", required=False)
    time_end = fields.Date("Evaluation end time", required=False)
    Job_Positions = fields.Many2one(comodel_name='hr.job', delegate=True)
    Department = fields.Many2one('hr.department')
    objectives_hr = fields.Selection([
        ('danhgiadinhky', 'Periodic evaluation'),
        ('danhgiagiahanhd', 'Contract renewal evaluation'),
        ('ddanhgiatangluong ', 'Salary increase evaluation'),
        ('danhgiathuviec', 'Probation evaluation')],
        string='Assessment objectives', default='danhgiadinhky')
    rate = fields.Selection([
        ('rate1', '0%'),
        ('rate2', '25%'),
        ('rate3', '50%'),
        ('rate4', '75%'),
        ('rate5', '100%')],
        string='Job completion rate', default='rate1')
    work_attitude = fields.Selection([
        ('w1', 'Bad'),
        ('w2', 'Good'),
        ('w3', 'Very good')],
        string='Work attitude', default='w2')

    work_productivity = fields.Integer("Work productivity", default='0')
    growth_at_work = fields.Text("Growth at work")

    absenteeism = fields.Selection([
        ('absenteeism1', '0%'),
        ('absenteeism2', '25%'),
        ('absenteeism3', '50%'),
        ('absenteeism4', '75%'),
        ('absenteeism5', '100%')],
        string='Absenteeism rate', default='absenteeism1')

    recruiting = fields.Selection([
        ('recruiting1', '0%'),
        ('recruiting2', '25%'),
        ('recruiting3', '50%'),
        ('recruiting4', '75%'),
        ('recruiting5', '100%')],
        string='Recruiting conversion rate', default='recruiting1')

    internal = fields.Selection([
        ('internal1', '0%'),
        ('internal2', '25%'),
        ('internal3', '50%'),
        ('internal4', '75%'),
        ('internal5', '100%')],
        string='Internal communication engagement rate', default='internal1')

    ot = fields.Float("Overtimes hours", default='0')
    rule = fields.Integer("Number of rule violation", default='0')
    comment = fields.Text()
    result = fields.Selection([
        ('rs1', 'Failed'),
        ('rs2', 'Passed')],
        string='Result')
    id = fields.Char(string='ID', required=True, copy=False, readonly=True,
                         default=lambda seft: _('New'))
    @api.model
    def create(self, vals):
        if vals.get('id', ('New')) == ('New'):
            vals['id'] = self.env['ir.sequence'].next_by_code('classlist.id') or _('New')
        res = super(hr_keypi, self).create(vals)
        return res

    @api.constrains('time_end')
    def onchange_end_dates(self):
        if (self.time_start and self.time_end) and (self.time_end < self.time_start):
            raise ValueError(('Time end must be greater than or equal to Time start.'))