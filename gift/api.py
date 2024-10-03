# gift/api.py

import frappe
from frappe.utils import now

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
