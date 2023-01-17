# Copyright 2016 LasLabs Inc.
# Copyright 2017 Kaushal Prajapati <kbprajapati@live.com>.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
# See https://pages.nist.gov/800-63-3/sp800-63b.html#memsecret

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ResCompany(models.Model):
    _inherit = "res.company"

    password_policy_enabled = fields.Boolean(default=False)

    # Verifiers SHOULD NOT require memorized secrets to be changed
    # arbitrarily (e.g., periodically).
    password_expiration = fields.Integer(
        "Days",
        default=0,
        help="How many days until passwords expire",
    )

    # Memorized secrets SHALL be at least 8 characters in length if
    # chosen by the subscriber.
    password_length = fields.Integer(
        "Characters",
        default=8,
        help="Minimum number of characters",
    )

    # Verifiers SHOULD NOT impose other composition rules (e.g.,
    # requiring mixtures of different character types or prohibiting
    # consecutively repeated characters) for memorized secrets.
    password_lower = fields.Integer(
        "Lowercase",
        default=0,
        help="Require number of lowercase letters",
    )
    password_upper = fields.Integer(
        "Uppercase",
        default=0,
        help="Require number of uppercase letters",
    )
    password_numeric = fields.Integer(
        "Numeric",
        default=0,
        help="Require number of numeric digits",
    )
    password_special = fields.Integer(
        "Special",
        default=0,
        help="Require number of unique special characters",
    )

    # Verifiers SHOULD offer guidance to the subscriber, such as a
    # password-strength meter.
    password_estimate = fields.Integer(
        "Estimation",
        default=3,
        help="Required score for the strength estimation. Between 0 and 4",
    )
    password_history = fields.Integer(
        "History",
        default=30,
        help="Disallow reuse of this many previous passwords - use negative "
        "number for infinite, or 0 to disable",
    )
    password_minimum = fields.Integer(
        "Minimum Hours",
        default=24,
        help="Amount of hours until a user may change password again",
    )

    @api.constrains("password_estimate")
    def _check_password_estimate(self):
        if self.password_estimate < 0 or self.password_estimate > 4:
            raise ValidationError(_("The estimation must be between 0 and 4."))
