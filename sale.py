# This file is part sale_margin_waiting module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from decimal import Decimal
from trytond.model import fields
from trytond.pool import Pool, PoolMeta

__all__ = ['Configuration', 'Sale']
__metaclass__ = PoolMeta


class Configuration:
    __name__ = 'sale.configuration'

    minimum_margin = fields.Numeric('Minimum Margin', digits=(16, 2),
        help='If the margin of a sale is less than this, the sale will '
        'required to be confirmed.')


class Sale:
    'Sale'
    __name__ = 'sale.sale'

    def check_for_quotation(self):
        Config = Pool().get('sale.configuration')
        super(Sale, self).check_for_quotation()
        config = Config(1)
        minimum_margin = (config.minimum_margin if config.minimum_margin
            else Decimal('0.0'))
        if self.margin <= minimum_margin:
            self.write([self], {
                'state': 'waiting',
            })
