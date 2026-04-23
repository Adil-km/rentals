import frappe

@frappe.whitelist()
def get_name():
    return "Adil KM"

def get_permission_query_conditions_for_vehicle(user):
    # return "name = 1"
    pass