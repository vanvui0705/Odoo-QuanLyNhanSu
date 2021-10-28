# -*- coding: utf-8 -*-

from odoo import models, fields, api


class business_keypi(models.Model):
    _name = "business.keypi"
    _description = "HR Management"

    # Employee = fields.One2many('hr.employee', 'employee_ids')
    id_bs = fields.Integer("ID", default='1')
    date_bs = fields.Datetime("Time of creation", required=False)
    time_startbs = fields.Date("Evaluation start time", required=False)
    time_endbs = fields.Date("Evaluation end time", required=False)
    Job_Positions = fields.Many2one(comodel_name='hr.job', delegate=True)
    Department = fields.Many2one('hr.department')
    objectives_bs = fields.Selection([
        ('danhgiadinhky', 'Periodic evaluation'),
        ('danhgiagiahanhd', 'Contract renewal evaluation'),
        ('ddanhgiatangluong ', 'Salary increase evaluation'),
        ('danhgiathuviec', 'Probation evaluation')],
        string='Assessment objectives', default='danhgiadinhky')
    rate_bs = fields.Selection([
        ('rate1', '0%'),
        ('rate2', '25%'),
        ('rate3', '50%'),
        ('rate4', '75%'),
        ('rate5', '100%')],
        string='Job completion rate', default='rate1')
    attitude_bs = fields.Selection([
        ('w1', 'Bad'),
        ('w2', 'Good'),
        ('w3', 'Very good')],
        string='Work attitude', default='w2')

    don_month = fields.Integer("Month Sales Bookings", default='0')
    dt_ll = fields.Integer("Sales by Contact Method", default='0')
    sale_rep = fields.Integer("Month Calls Sales Rep", default='0')

    rate_cd = fields.Selection([
        ('tylechotdon1', '0%'),
        ('tylechotdon2', '25%'),
        ('tylechotdon3', '50%'),
        ('tylechotdon4', '75%'),
        ('tylechotdon5', '100%')],
        string='Quote To Close Ratio', default='tylechotdon1')

    lts = fields.Selection([
        ('lts1', '0%'),
        ('lts2', '25%'),
        ('lts3', '50%'),
        ('lts4', '75%'),
        ('lts5', '100%')],
        string='Lead-to-Sale %', default='lts1')

    churn_rates = fields.Selection([
        ('churn_rates1', '0%'),
        ('churn_rates2', '25%'),
        ('churn_rates3', '50%'),
        ('churn_rates4', '75%'),
        ('churn_rates5', '100%')],
        string='Churn Rates', default='churn_rates1')

    growth_bs = fields.Integer("Monthly Sales Growth", default='0')
    ot_bs = fields.Float("Overtimes hours", default='0')
    rule_bs = fields.Integer("Number of rule violation", default='0')
    Comment_bs = fields.Text(string="Comment")
    result_bs = fields.Selection([
        ('rs1','Failed'),
        ('rs2','Passed')],
        string='Result')

    @api.constrains('time_endbs')
    def onchange_end_dates(self):
        if (self.time_startbs and self.time_endbs) and (self.time_endbs < self.time_startbs):
            raise ValueError(('Time end must be greater than or equal to Time start.'))