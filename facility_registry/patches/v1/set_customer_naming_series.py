import frappe
def execute(): 
	selling_settings = frappe.get_doc('Selling Settings')
	selling_settings.customer_naming_by = 'Naming Series'
	selling_settings.save()