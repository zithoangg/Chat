
import json
import os
import azure.functions as func

STORAGE_FILE = os.path.join(os.path.dirname(__file__), '../shared/messages.json')

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        if not os.path.exists(STORAGE_FILE):
            return func.HttpResponse("[]", mimetype="application/json")

        with open(STORAGE_FILE, 'r') as f:
            messages = json.load(f)

        return func.HttpResponse(json.dumps(messages), mimetype="application/json")
    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
