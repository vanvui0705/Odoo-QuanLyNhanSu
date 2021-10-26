# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hr_kpi (models.Model):
    _name = "hr.kpi"
    _description = "HR Management"

    # id = fields.Char(string='ID', required=True, copy=False, readonly=True,
    #                  default=lambda seft: _('New'))
    # @api.model
    # def create(self, vals):
    #     if vals.get('id', ('New')) == ('New'):
    #         vals['id'] = self.env['ir.sequence'].next_by_code('classlist.id') or _('New')
    #     res = super(hr_kpi, self).create(vals)
    #     return res


    # Employee = fields.One2many('hr.employee', 'employee_ids')
    number = fields.Integer("Number", default= '1')
    date = fields.Datetime("Time of creation", required=False)
    time_start = fields.Date("Evaluation start time", required=False)
    time_end = fields.Date("Evaluation end time", required=False)

    objectives = fields.Selection([
        ('danhgiadinhky', 'Periodic evaluation'),
        ('danhgiagiahanhd', 'Contract renewal evaluation'),
        ('ddanhgiatangluong ', 'Salary increase evaluation'),
        ('danhgiathuviec', 'Probation evaluation')],
        string='Assessment objectives', default='Periodic evaluation')




    class key_hr(models.Model):
        _name = "key.hr"

        key_hr_id = fields.Char('Id', default=1)
        rate = fields.Selection([
            ('rate1', '0%'),
            ('rate2', '25%'),
            ('rate3', '50%'),
            ('rate4', '75%'),
            ('rate5', '100%')],
            string='Job completion rate', default='0%')
        Work_attitude = fields.Selection([
            ('w1', 'Bad'),
            ('w2', 'Good'),
            ('w3', 'Very good')],
            string='Work attitude', default='Good')

        Work_productivity = fields.Integer("Work productivity", default='0')
        Growth_at_work = fields.Text("Growth at work")

        absenteeism = fields.Selection([
            ('absenteeism1', '0%'),
            ('absenteeism2', '25%'),
            ('absenteeism3', '50%'),
            ('absenteeism4', '75%'),
            ('absenteeism5', '100%')],
            string='Absenteeism rate', default='0%')

        recruiting = fields.Selection([
            ('recruiting1', '0%'),
            ('recruiting2', '25%'),
            ('recruiting3', '50%'),
            ('recruiting4', '75%'),
            ('recruiting5', '100%')],
            string='Recruiting conversion rate', default='0%')

        internal = fields.Selection([
            ('Internal1', '0%'),
            ('Internal2', '25%'),
            ('Internal3', '50%'),
            ('Internal4', '75%'),
            ('Internal5', '100%')],
            string='Internal communication engagement rate', default='0%')

        #ot = fields.Integer("Overtimes hours", default='0')
        #rule = fields.Integer("Number of rule violation", default='0')




