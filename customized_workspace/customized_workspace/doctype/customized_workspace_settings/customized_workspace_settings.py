# Copyright (c) 2023, Anupam Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CustomizedWorkspaceSettings(Document):
	def get_roles(self):
		return [row.role for row in self.applicable_for_roles]
