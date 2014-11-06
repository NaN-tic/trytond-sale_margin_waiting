#!/usr/bin/env python
# This file is part sale_margin_waiting module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_depends


class SaleMarginWaitingTestCase(unittest.TestCase):
    'Test Sale Margin Waiting module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('sale_margin_waiting')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleMarginWaitingTestCase))
    return suite
