import frappe

def after_insert(self,method):

    if self.status != "Ringing":
        to_number = frappe.db.get_value("Lead",{"mobile_no":self.to},"name")
        if to_number:
            self.append("links",{
                "link_doctype": "Lead",
                "link_name":to_number,
                "link_title":to_number
            })
