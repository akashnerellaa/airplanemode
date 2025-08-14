# Copyright (c) 2023,  Akash Nerella and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FlightPassenger(Document):
 def before_save(self):
  #self.validate()
  if self.last_name:
   self.full_name = self.first_name + " " + self.last_name
  else:
    self.full_name= self.first_name
    
      

# def validate(self):
 # if not self.first_name:
  #  self.throw("First name is mandatory.")
  #if not self.last_name:
   # self.throw("Last name is mandatory.")
   
         
        
