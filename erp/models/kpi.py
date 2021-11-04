# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kpi(models.Model):
    _name = "kpi"
    _description = "HR Management"


    employee = fields.Many2one('hr.employee', 'name', Required=True)
    id_employee = fields.Char('ID Employee', required=True)
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
    set_of_criteria_1 = fields.One2many(comodel_name='business', inverse_name='id')
    set_of_criteria_2 = fields.One2many(comodel_name='kpi.product', inverse_name='id')
    set_of_criteria_3 = fields.One2many(comodel_name='kpi.hr', inverse_name='id')

class business(models.Model):
    _name = "business"
    _description = "HR Management"


    id = fields.Char(string='ID', required=True, copy=False, readonly=True,
                         default=lambda seft: ('New'))
    @api.model
    def create(self, vals):
        if vals.get('id', ('New')) == ('New'):
            vals['id'] = self.env['ir.sequence'].next_by_code('business.id') or ('New')
        res = super(business, self).create(vals)
        return res

    criteria_name = fields.Selection([
        ('revenue', 'Revenue'),
        ('customers_number', 'Customers number'),
        ('number_of_satisfied_customers', 'Number of satisfied customers'),
        ('monthly_sales_growth ', 'Monthly Sales Growth '),
        ('quote_to_close_ratio ', 'Quote To Close Ratio ')],
        string='Criteria name', default='revenue')

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

    criteria_name = fields.Selection([
        ('Number of products produced', 'Number of products produced'),
        ('rate of damaged products', 'Rate of damaged products '),
        ('Raw material usage norms', 'Raw material usage norms '),
        ('Allowable material consumption rate', 'Allowable material consumption rate '),
        ('Material damage rate', 'Material damage rate'),
    ],
        string='Criteria name', default='Number of products produced')
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
    criteria_name = fields.Selection([
        ('Number of Curriculum Vitae', 'Number of Curriculum Vitae'),
        ('Interview rate/total number of CVs', 'Interview rate/total number of CVs '),
        ('Recruiting conversion rate', 'Recruiting conversion rate '),
        ('Employee complaint rate', 'Employee complaint rate '),
        ('Accuracy rate of salary payment report', 'Accuracy rate of salary payment report'),
    ],
        string='Criteria name', default='Number of Curriculum Vitae')
    target = fields.Integer("Target", default='')
    Actual = fields.Integer("Actual", default='')
    per_Complete = fields.Integer("Percent complete", default='')
    Score = fields.Integer("Score", default='')










