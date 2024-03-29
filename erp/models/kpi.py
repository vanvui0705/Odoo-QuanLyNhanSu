# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kpi(models.Model):
    _name = "kpi"
    _description = "HR Management"


    employee = fields.Many2one('hr.employee', 'name', Required=True,)
    # id_employee = fields.Char('ID Employee', required=True)
    # id_bs = fields.Integer("ID", default='1')
    id = fields.Char(string='ID', required=True, copy=False, readonly=True,
                         default=lambda seft: ('New'))
    @api.model
    def create(self, vals):
        if vals.get('id', ('New')) == ('New'):
            vals['id'] = self.env['ir.sequence'].next_by_code('classlist.id') or ('New')
        res = super(kpi, self).create(vals)
        return res
    date_bs = fields.Datetime("Time of creation", required=False)
    time_startbs = fields.Date("Evaluation start time", required=False)
    time_endbs = fields.Date("Evaluation end time", required=False)
    Job_Positions = fields.Many2one(comodel_name='hr.job', delegate=True)
    Department = fields.Many2one('hr.department', delegate=True)
    objectives_bs = fields.Selection([
        ('danhgiadinhky', 'Periodic evaluation'),
        ('danhgiagiahanhd', 'Contract renewal evaluation'),
        ('ddanhgiatangluong ', 'Salary increase evaluation'),
        ('danhgiathuviec', 'Probation evaluation')],
        string='Assessment objectives', default='danhgiadinhky')
    ot_bs = fields.Float("Overtimes hours", default='0')
    rule_bs = fields.Integer("Number of rule violation", default='0')
    Absenteeism_rate = fields.Integer("Number of absences", default='0')
    Work_attitude = fields.Selection([
        ('Very good ', 'Very good '),
        ('Good ', 'Good '),
        ('Bad', 'Bad')],
        string='Work attitude', default='Good')
    Total_rating_score = fields.Integer("Medium score", default='0')
    set_of_criteria_1 = fields.Many2many(comodel_name='business', inverse_name='id')
    set_of_criteria_2 = fields.Many2many(comodel_name='kpi.product', inverse_name='id')
    set_of_criteria_3 = fields.Many2many(comodel_name='kpi.hr', inverse_name='id')

    # def print_report(self):
    #     data = {
    #
    #     }
    #     # docids = self.env['sale.order'].search([]).ids
    #     return self.env.ref('erp.kpiemployee_report').report_action(None, data=data)

class business(models.Model):
    _name = "business"
    _description = "HR Management"


    # id = fields.Char(string='ID', required=True, copy=False, readonly=True,
    #                      default=lambda seft: ('New'))
    # @api.model
    # def create(self, vals):
    #     if vals.get('id', ('New')) == ('New'):
    #         vals['id'] = self.env['ir.sequence'].next_by_code('business.id') or ('New')
    #     res = super(business, self).create(vals)
    #     return res

    criteria_name = fields.Many2one('criteria.2', 'name', Required=True, delegate=True)
    target = fields.Integer("Target", default='')
    Actual = fields.Integer("Actual", default='')
    per_Complete = fields.Integer("Percent complete", default='')
    Score = fields.Integer("Score", default='')





class kpi_product(models.Model):
    _name = "kpi.product"
    _description = "KPI product department"

    id = fields.Char(string='ID', required=True, copy=False, readonly=True,
                         default=lambda seft: ('New'))
    @api.model
    def create(self, vals):
        if vals.get('id', ('New')) == ('New'):
            vals['id'] = self.env['ir.sequence'].next_by_code('kpi_product.id') or ('New')
        res = super(kpi_product, self).create(vals)
        return res

    criteria_name = fields.Many2one('criteria.1', 'name', Required=True,delegate=True)
    target = fields.Integer("Target", default='')
    Actual = fields.Integer("Actual", default='')
    per_Complete = fields.Integer("Percent complete", default='')
    Score = fields.Integer("Score", default='')


class kpi_hr(models.Model):
    _name = "kpi.hr"
    _description = "KPI HR department"


    id = fields.Char(string='ID', required=True, copy=False, readonly=True,
                     default=lambda seft: ('New'))

    @api.model
    def create(self, vals):
        if vals.get('id', ('New')) == ('New'):
            vals['id'] = self.env['ir.sequence'].next_by_code('kpi_hr.id') or ('New')
        res = super(kpi_hr, self).create(vals)
        return res
    criteria_name = fields.Many2one('criteria', 'name', Required=True)
    target = fields.Integer("Target", default='')
    Actual = fields.Integer("Actual", default='')
    per_Complete = fields.Integer("Percent complete", default='')
    Score = fields.Integer("Score", default='')



class criteria(models.Model):
    _name = "criteria"
    _description = " "
    _order = 'name'

    name = fields.Char('Criteria name', store=True, readonly=False, tracking=True)


class criteria_1(models.Model):
    _name = "criteria.1"
    _description = " "
    _order = 'name'

    name = fields.Char('Criteria name', store=True, readonly=False, tracking=True)

class criteria_2(models.Model):
    _name = "criteria.2"
    _description = " "
    _order = 'name'

    name = fields.Char('Criteria name', store=True, readonly=False, tracking=True)






