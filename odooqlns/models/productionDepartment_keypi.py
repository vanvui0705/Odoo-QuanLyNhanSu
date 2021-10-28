from odoo import models, fields, api


class production_keypi(models.Model):
    _name = "production.keypi"
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
    rate = fields.Selection([
        ('rate1', '0%'),
        ('rate2', '25%'),
        ('rate3', '50%'),
        ('rate4', '75%'),
        ('rate5', '100%')],
        string='Faulty goods rate', default='rate1')
    attitude = fields.Selection([
        ('a1', 'Bad'),
        ('a2', 'Good'),
        ('a3', 'Very good')],
        string='Work attitude', default='a1')

    productivity = fields.Integer("Labor productivity", default='1')
    target = fields.Char("Production target", required=True)

    regulations = fields.Selection([
        ('regulation1', '0%'),
        ('regulation2', '25%'),
        ('regulation3', '50%'),
        ('regulation4', '75%'),
        ('regulation5', '100%')],
        string='Rate of Violation of Production regulations', default='regulation1')

    material = fields.Selection([
        ('material0', '0%'),
        ('material1', '1%'),
        ('material2', '2%'),
        ('material3', '3%'),
        ('material4', '4%'),
        ('material5', '5%'),
        ('material6', '6%'),
        ('material7', '7%'),
        ('material8', '8%'),
        ('material9', '9%'),
        ('material10', '10%'),],
        string='Material loss rate', default='material0')

    overtime = fields.Float("Overtimes", default='0')
    comment = fields.Text(string="Comment")
    result = fields.Selection([
        ('rs1','Failed'),
        ('rs2','Passed')],
        string='Result')

    @api.constrains('time_endbs')
    def onchange_end_dates(self):
        if (self.time_startbs and self.time_endbs) and (self.time_endbs < self.time_startbs):
            raise ValueError(('Time end must be greater than or equal to Time start.'))