# Copyright (c) 2026, AdilKM and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Driver(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		first_name: DF.Data
		full_name: DF.Data | None
		last_name: DF.Data
		license_number: DF.Data
		phone_number: DF.Data
		profile_image: DF.AttachImage | None
	# end: auto-generated types

	def before_save(self):
		self.full_name = f"{self.first_name} {self.last_name}"
