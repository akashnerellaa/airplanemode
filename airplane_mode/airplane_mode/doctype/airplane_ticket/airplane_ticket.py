# Copyright (c) 2023, Akash Nerella and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

from frappe import db
from random import randint, choice

class AirplaneTicket(Document):
 
    
 def before_save(self):
     self.set_total_amount()
     #self.before_insert_airplane_ticket()
     self.validate_flight_capacity()
  
 def validate(self):
        self.del_duplicated()
        
 # def before_insert(self):
  #  self.validate_capacity()

 def set_total_amount(self):
     self.total_amount= int(self.flight_price) + sum(item.amount for item in self.add_ons)
     
 def before_submit(self):
      self.validate_status()
     

 
 def del_duplicated(self):
        unique_elements = []
        for row in self.add_ons:
            if row.item in unique_elements:
                self.add_ons.remove(row)
            else:
                unique_elements.append(row.item)
       
       
 def validate_status(self):
    if self.status != "Boarded":
        frappe.throw(
            "Sorry Cant Submit The Document Until Passenger is Boarded"
        )
        """ 
 def before_insert_airplane_ticket(self):
    
    #Generates a random seat number and sets it on the Airplane Ticket before inserting it into the database.
    
    # Generate a random integer between 1 and 99 (inclusive)
    random_integer = randint(1, 99)

    # Choose a random character from all uppercase and lowercase letters
    random_character = choice("ABCDE")

    # Generate the final seat number
    self.seat = f"{random_integer}{random_character}"

    # Set the seat number on the Airplane Ticket
    #self.seat = seat_number  
     """           
                
  # Assuming you have a method like this in your Airplane Ticket DocType
 def validate_flight_capacity(self):
    # Check if it's a new ticket being created
    if self.doctype == "Airplane Ticket" and self.is_new:
        # Extract relevant information
        flight = frappe.get_doc('Airplane Flight', self.flight)
        airplane = frappe.get_doc('Airplane', flight.airplane)
        num_of_tix = frappe.db.count('Airplane Ticket', filters={
            'flight': flight.name
        })

        # Validate capacity
        if num_of_tix > airplane.capacity:
            frappe.throw("Unable to create new ticket: This flight has been fully booked")


 
  

  # Other validation logic
