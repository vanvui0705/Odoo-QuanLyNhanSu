from odoo import models, fields, api


class finance_keypi(models.Model):
    _name = "finance.keypi"
    _description = "HR Management"

    # Employee = fields.One2many('hr.employee', 'employee_ids')
    # id_bs = fields.Integer("ID", default='1')
    employee = fields.Many2one('hr.employee', 'name', Required=True)
    id = fields.Char(string='ID', required=True, copy=False, readonly=True,
                     default=lambda seft: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('id', ('New')) == ('New'):
            vals['id'] = self.env['ir.sequence'].next_by_code('finance_keypi.id') or _('New')
        res = super(finance_keypi, self).create(vals)
        return res
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

    attitude = fields.Selection([
        ('a1', 'Bad'),
        ('a2', 'Good'),
        ('a3', 'Very good')],
        string='Work attitude', default='a1')
    productivity = fields.Integer("Labor productivity", default='1')
    target = fields.Char("Finance target", required=True)

    regulations = fields.Selection([
        ('regulation1', '0%'),
        ('regulation2', '25%'),
        ('regulation3', '50%'),
        ('regulation4', '75%'),
        ('regulation5', '100%')],
        string='Rate of Violation of Finance regulations', default='regulation1')

    report = fields.Selection([
        ('report0', '0%'),
        ('report1', '10%'),
        ('report2', '20%'),
        ('report3', '30%'),
        ('report4', '40%'),
        ('report5', '50%'),
        ('report6', '60%'),
        ('report7', '70%'),
        ('report8', '80%'),
        ('report9', '90%'),
        ('report10', '100%'),],
        string='Financial Reporting Error Rate', default='report0')

    overtime = fields.Float("Overtimes", default='0')
    numberRP = fields.Integer("Number of reports", default='1')
    Comment_bs = fields.Text(string="Comment")
    result_bs = fields.Selection([
        ('rs1','Failed'),
        ('rs2','Passed')],
        string='Result')

    @api.constrains('time_endbs')
    def onchange_end_dates(self):
        if (self.time_startbs and self.time_endbs) and (self.time_endbs < self.time_startbs):
            raise ValueError(('Time end must be greater than or equal to Time start.'))