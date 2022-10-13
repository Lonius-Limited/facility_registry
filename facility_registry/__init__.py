__version__ = '0.0.1'
import frappe
import requests, json
from frappe.contacts.doctype.contact.contact import get_default_contact
URL ="https://exchange.lonius.cloud"
API ="/api/method/exchange.api.facility_registry.utils.create_credentials"

def create_facility_user(doc, state):
    if not doc.customer_type=="Company": return
    if doc.facility_access_details: return
    email = get_facility_email(doc.name)
    facility_name = doc.name
    payload = dict(email=email,facility_name=facility_name)
    r = requests.post(f"{URL}{API}", json=dict(payload=payload))
    frappe.msgprint(f"{r.json()}")
    doc.set("facility_access_details",r.json())
def get_facility_email(facility):
    default_contact= get_default_contact("Customer",facility)
    if not default_contact: return ""
    contact_document = frappe.get_doc("Contact",default_contact )
    email_ids = contact_document.email_ids
    if not email_ids: return ""
    email_arr= [x.get("email_id") for x in email_ids]
    if not email_arr: return ""
    return email_arr[0]
