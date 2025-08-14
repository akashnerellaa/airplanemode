# Copyright (c) 2023,  Akash Nerella and contributors
# For license information, please see license.txt
import frappe
#from frappe import qb

def execute(filters=None):
 columns = [
     {
            "fieldtype": "Link",
            "label": "Airline",
            "fieldname": "airline",
            "options":"Airline",
            "width": 200,
        },
        {
            "fieldtype": "Currency",
            "label": "Revenue",
            "fieldname": "revenue",
            "width": 200,
        }
        
 ]
    
 data = frappe.db.sql(
            """
        SELECT
            al.name as airline,
            sum(at.total_amount) as revenue
        FROM
            `tabAirplane Ticket` at
            JOIN `tabAirplane Flight` af ON at.flight = af.name
            JOIN `tabAirplane` ap ON af.airplane = ap.name
            RIGHT JOIN `tabAirline` al ON ap.airline = al.name
        GROUP BY
            al.name
        ORDER BY
            revenue desc
        """
        )
 chart = {
    "type":"donut",
    "data":{
        "labels": [row[0] for row in data],
        "datasets":[
            {
            "values":[row[1] for row in data]
        }
            ]
    }
 }
 
 total_revenue = sum((row[1] or 0) for row in data)
 
 report_summary = [
     {
         "value": total_revenue,
         "indicator": "green" if total_revenue > 0 else "red",
         "label" : "Total Revenue",
         "datatype" : "Currency",
     }
 ]
 

 #data = (row for row in data if row.revenue >0) if you want to remove airline with zero revenue use this

 return columns, data, None, chart, report_summary

