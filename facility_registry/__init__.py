__version__ = '0.0.1'
import frappe
import requests, json
from frappe.contacts.doctype.contact.contact import get_default_contact
from stripe import api_key
URL ="https://exchange.lonius.cloud"
API ="/api/method/exchange.api.facility_registry.utils.create_credentials"
api_key ="ca57caee4c7c51e"
api_secret ="12174345b1c9a06"
headers = dict(Authorization=f'token {api_key}:{api_secret}')

def create_facility_user(doc, state):
    if not doc.customer_type=="Company": return
    if doc.facility_access_details: return
    email = get_facility_email(doc.name)
    facility_name = doc.customer_name
    facility_id = doc.name
    params = dict(email = email, facility_name = facility_name, facility_id = facility_id)
    r = requests.get(f"{URL}{API}", headers=headers, payload=params)
    frappe.msgprint(f"{r.json()}")
    doc.set("facility_access_details",r.json())
def get_facility_email(facility):
    default_contact= get_default_contact("Customer",facility)
    if not default_contact: return ""
    contact_document = frappe.get_doc("Contact",default_contact )
    email_ids = contact_document.email_ids
    if not email_ids: return ""
    email_arr = [x.get("email_id") for x in email_ids]
    if not email_arr: return ""
    return email_arr[0]
