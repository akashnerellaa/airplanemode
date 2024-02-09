// Copyright (c) 2023, Mohammed Anas and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
    refresh(frm) {
        frm.add_custom_button("Assign Seat", () => {
            const dialog = new frappe.ui.Dialog({
                title: "Select Seat", // Specify your custom title here
                fields: [
                    {
                        fieldtype: 'Data',
                        label: 'Seat Number',
                        fieldname: 'assign_seat',
                        reqd: 1,
                    },
                ],
                primary_action: function () {
                    const data = dialog.get_values();
                    if (data) {
                        frm.set_value('seat', data.assign_seat);
                        frm.save();
                        dialog.hide();
                    }
                },
                primary_action_label: 'Save',
            });
            dialog.show();
        });
    },
});
