
import json
import os
import azure.functions as func

STORAGE_FILE = os.path.join(os.path.dirname(__file__), '../shared/messages.json')

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
        username = data.get("username")
        message = data.get("message")

        if not username or not message:
            return func.HttpResponse("Missing fields", status_code=400)

        if not os.path.exists(STORAGE_FILE):
            with open(STORAGE_FILE, 'w') as f:
                json.dump([], f)

        with open(STORAGE_FILE, 'r') as f:
            messages = json.load(f)

        messages.append({"username": username, "message": message})
        messages = messages[-50:]

        with open(STORAGE_FILE, 'w') as f:
            json.dump(messages, f)

        return func.HttpResponse("Message sent", status_code=200)
    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
