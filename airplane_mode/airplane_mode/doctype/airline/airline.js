// Copyright (c) 2023, Mohammed Anas and contributors
// For license information, please see license.txt

 
frappe.ui.form.on("Airline", {
 	refresh(frm) {
		frm.add_web_link(__('Visit Website'), function() {
            var website = frm.doc.website;
            if (website) {
                frm.add_web_link(website);
            } else {
                frappe.msgprint(__('No website link available.'));
            }
        });
        
          

 	},
 });
