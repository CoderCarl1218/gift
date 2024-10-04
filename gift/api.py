import frappe
from frappe.utils import now
from frappe.utils import today



def update_item_summary(doc, method=None):
    """
    Update or create an Item Summary entry based on the Items document.
    """
    # Log the received document for debugging
    frappe.logger().info(f"Received update_item_summary doc: {doc.as_dict()}")

    # Extract fields using consistent names
    item_code = doc.item_code
    item_name = doc.item_name
    quantity = doc.item_quantity

    # Validate presence of required fields
    if not item_code or not item_name or quantity is None:
        frappe.throw("Missing 'item_code', 'item_name', or 'item_quantity' in the Items document.")

    # Convert quantity to a numeric type
    try:
        quantity = float(quantity)
    except ValueError:
        frappe.throw("Invalid value for 'item_quantity'. It must be a number.")

    # Fetch the existing Item Summary by item_code
    item_summary_name = frappe.db.get_value("Item Summary", {"item_code": item_code}, "name")

    if not item_summary_name:
        # Create a new Item Summary if it doesn't exist
        item_summary_doc = frappe.get_doc({
            "doctype": "Item Summary",
            "item_code": item_code,
            "item_name": item_name,
            "total_quantity": quantity,
            "last_updated": now()
        })
        item_summary_doc.insert()
        frappe.logger().info(f"Created new Item Summary for item_code: {item_code}, item_name: {item_name}, quantity: {quantity}")
    else:
        # Update the existing Item Summary
        item_summary_doc = frappe.get_doc("Item Summary", item_summary_name)
        item_summary_doc.total_quantity += quantity  # Increment by the added quantity
        item_summary_doc.last_updated = now()
        item_summary_doc.save()
        frappe.logger().info(f"Updated Item Summary for item_code: {item_code}, item_name: {item_name} with added quantity: {quantity}")

    frappe.db.commit()
    return "Success"

def cancel_stock_balance(doc, method=None):
    """
    Reverse the quantity in Item Summary upon cancellation of an Items document.
    """
    # Log the received document for debugging
    frappe.logger().info(f"Received cancel_stock_balance doc: {doc.as_dict()}")

    # Extract fields using consistent names
    item_code = doc.item_code
    item_name = doc.item_name
    quantity = doc.item_quantity

    # Validate presence of required fields
    if not item_code or not item_name or quantity is None:
        frappe.throw("Missing 'item_code', 'item_name', or 'item_quantity' in the Items document.")

    # Convert quantity to a numeric type
    try:
        quantity = float(quantity)
    except ValueError:
        frappe.throw("Invalid value for 'item_quantity'. It must be a number.")

    # Fetch the existing Item Summary by item_code
    item_summary_name = frappe.db.get_value("Item Summary", {"item_code": item_code}, "name")

    if item_summary_name:
        # Reverse the quantity as the stock balance is canceled
        item_summary_doc = frappe.get_doc("Item Summary", item_summary_name)
        item_summary_doc.total_quantity -= quantity
        item_summary_doc.last_updated = now()
        item_summary_doc.save()
        frappe.logger().info(f"Cancelled Item Summary for item_code: {item_code}, item_name: {item_name} with subtracted quantity: {quantity}")
        frappe.db.commit()
    else:
        frappe.throw(f"No Item Summary found for item_code: {item_code}")

    return "Cancelled"

def validate_item_quantity(doc, method=None):
    """
    Validate that the item_quantity is not negative.
    """
    if doc.item_quantity < 0:
        frappe.throw("Item Quantity cannot be negative.")
import frappe
from frappe.utils import today
import logging

logger = logging.getLogger(__name__)

import frappe
from frappe.utils import today
import logging

logger = logging.getLogger(__name__)

def send_birthday_emails():
    """
    Sends Birthday Template emails with PDF attachments to customers whose birthday is today.
    """
    try:
        today_date = today()  # Format: 'YYYY-MM-DD'
        today_month = int(today_date[5:7])  # Extract month as integer
        today_day = int(today_date[8:10])    # Extract day as integer

        logger.info(f"Initiating birthday email process for {today_date}.")

        # SQL query to fetch customers with today's birthday
        query = """
            SELECT name, full_name, email, customer_code
            FROM `tabCustomers`
            WHERE MONTH(birthday) = %s AND DAY(birthday) = %s
        """
        customers = frappe.db.sql(query, (today_month, today_day), as_dict=True)

        logger.info(f"Found {len(customers)} customer(s) with birthdays today.")

        for customer in customers:
            try:
                # Validate email
                if not customer.email:
                    logger.warning(f"Customer {customer.full_name} does not have an email address. Skipping.")
                    continue

                # Generate PDF using the "Birthday Template" Print Format
                pdf = frappe.get_print('Customers', customer.name, 'Test Format', as_pdf=True)

                # Prepare email details
                email_subject = f"Happy Birthday, {customer.full_name}!"
                email_template = frappe.get_doc("Email Template", "Birthday Greeting")
                email_message = frappe.render_template(email_template.message, {"doc": customer})

                # Send Email with PDF Attachment
                frappe.sendmail(
                    recipients=[customer.email],
                    subject=email_subject,
                    message=email_message,
                    reference_doctype='Customers',
                    reference_name=customer.name,
                    attachments=[{
                        'fname': f"Happy_Birthday_{customer.full_name}.pdf",
                        'fcontent': pdf
                    }]
                )

                logger.info(f"Birthday email with PDF sent to {customer.full_name} at {customer.email}.")

            except Exception as e:
                logger.error(f"Failed to send email to {customer.full_name} ({customer.email}): {e}")

    except Exception as e:
        logger.error(f"Error in send_birthday_emails: {e}")
        # Optional: Notify administrators about the failure
        # frappe.sendmail(
        #     recipients=["admin@example.com"],
        #     subject="Birthday Email Script Failed",
        #     message=f"An error occurred while sending birthday emails:\n\n{e}"
        # )
