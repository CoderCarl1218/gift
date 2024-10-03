# Copyright (c) 2024, SERVIO Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Customers(Document):
	def before_save(self):
    	 self.full_name = f"{self.first_name} {self.last_name}"
