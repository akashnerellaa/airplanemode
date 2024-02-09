# your_custom_app/your_custom_app/your_custom_app/send_email_notifications.py

import frappe



#  def send_email_notifications():
#     contracts_to_notify = frappe.get_all("Shop Contract", filters={"fulfillment_status": "Signed"})
#     for contract in contracts_to_notify:
#         send_email(contract)

#  def send_email(contract):
#     # Get customer email from the related customer field in the contract
#     email = frappe.get_all("Shop Contract", {"tenant_mail_id"})
#     # Prepare and send the email using frappe.sendmail
#     subject = "Monthly Fulfillment Status Update"
#     message = f"Dear Customer, your contract with ID {contract.tenant_name} is in 'Signed' fulfillment status."
    
#     frappe.sendmail(
#         recipients=[email],
#         subject=subject,
#         message=message
#     )
 
def send_email_notifications():
    contracts_to_notify = frappe.get_all("Shop Contract", filters={"fulfillment_status": "Signed"},fields=["tenant_mail_id"])
    for contract in contracts_to_notify:
        send_email(contract)

def send_email(contract):
    email = contract.tenant_mail_id  # Get email directly from the contract
    if email :
        subject = "Monthly Fulfillment Status Update"
        message = f"Dear Customer, your contract with ID {contract.name} is in 'Signed' fulfillment status."
        frappe.sendmail(recipients=[email], subject=subject, message=message)
        print(f"Sent email to {email}")  # Add logging for confirmation
    else:
        print(f"Contract {contract.name} has no email address.{contract.tenant_mail_id}")  # Handle missing email