# This file is part of the sale_margin_waiting module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class SaleMarginWaitingTestCase(ModuleTestCase):
    'Test Sale Margin Waiting module'
    module = 'sale_margin_waiting'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleMarginWaitingTestCase))
    return suite