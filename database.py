import os
from supabase import create_client, Client

class SupabaseManager:
    def __init__(self):
        # DNA Section 6: Zero-Hardcode Policy
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
        
        if not url or not key:
            raise ValueError("Missing Supabase Credentials in Environment Variables")
            
        self.supabase: Client = create_client(url, key)

    def save_product(self, product_id, product_name, raw_json, prompt):
        data = {
            "product_id": product_id,
            "product_name": product_name,
            "raw_json": raw_json,
            "positive_prompt": prompt
        }
        # Upsert logic to prevent duplicate errors
        return self.supabase.table("tiktok_products").upsert(data).execute()

    def log_event(self, event_type, status, payload=None):
        log_data = {
            "event_type": event_type,
            "status": status,
            "payload": payload or {}
        }
        return self.supabase.table("automation_logs").insert(log_data).execute()

if __name__ == "__main__":
    print("Supabase Manager Initialized. Ready for Data Injection.")
