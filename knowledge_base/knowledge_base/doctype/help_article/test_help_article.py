# Copyright (c) 2013, Frappe and Contributors
# See license.txt

import frappe
import unittest

test_records = frappe.get_test_records('Help Article')

class TestHelpArticle(unittest.TestCase):
	pass
