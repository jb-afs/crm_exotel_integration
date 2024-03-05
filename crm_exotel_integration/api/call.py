import frappe
import requests

@frappe.whitelist()
def initiating_call_numbers(from_number,to_number,caller_id):
    exotel_details = frappe.get_doc("CRM Exotel Settings")
    if not exotel_details.enabled:
        frappe.throw("Please Enabled CRM Exotel Settings!")
    
    exotel_api_key = exotel_details.api_key
    exotel_api_token = exotel_details.api_token
    exotel_account_sid = exotel_details.account_sid
    subdomain = exotel_details.subdomain

    logs_url = "https://{api_key}:{api_token}{subdomain}/v1/Accounts/{account_sid}/Calls/connect".format(api_key=exotel_api_key,api_token =exotel_api_token,subdomain=subdomain, account_sid = exotel_account_sid)

    res = requests.get(logs_url)
    res_json = res.json()
    frappe.log_error("employee checkin check",message="Response Status : {}, data : {}".format(res.status_code,res_json))