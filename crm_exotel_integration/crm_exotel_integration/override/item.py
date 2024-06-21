import frappe         

def validate(self, method):
    if self.custom_ageing_in_days is not None:
        ageing_buckets = frappe.get_all("Ageing Bucket", fields=["name", "min_value", "max_value"])
        custom_ageing_in_days = int(self.custom_ageing_in_days)
        
        self.custom_ageing_bucket = None 
        
        for bucket in ageing_buckets:
            min_value = int(bucket['min_value'])
            max_value = int(bucket['max_value'])
            
            if min_value <= custom_ageing_in_days <= max_value:
                self.custom_ageing_bucket = bucket['name']
                break
