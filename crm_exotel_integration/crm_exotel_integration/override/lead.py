import frappe        

def validate(self, method):
    if self.custom_ageing_in_days:
        ageing_buckets = frappe.get_all("Ageing Bucket", fields=["name", "min_value", "max_value"])
        for bucket in ageing_buckets:
            if bucket['min_value'] <= str(self.custom_ageing_in_days) <= bucket['max_value']:
                self.custom_ageing_bucket = bucket['name']
                break
        else:
            self.custom_ageing_bucket = None 
