# Copyright (c) 2023, Mohammed Anas and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
 def on_submit(self):
    """
    Set the Status field to Completed after the Airplane Flight document is submitted.
    """
    self.status = "Completed"
    