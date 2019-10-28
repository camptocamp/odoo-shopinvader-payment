# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class PaymentTransaction(models.Model):

    _inherit = "payment.transaction"

    def _get_invader_payables(self):
        self.ensure_one()
        if self.partner_id:
            return self.partner_id
        return super(PaymentTransaction, self)._get_invader_payables()
