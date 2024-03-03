from flask import Flask, request, jsonify
from db import Connection
from grazie_utils import *
from assistants import *
import json

app = Flask(__name__)
db = Connection("codding_tasks_db")
tasks_collection = db.tasks


weakness_collection =db.weakness

# Assitents

vlada = CodeValidator()
vesna = Vesna()
vid = Vid()
veles = Veles()



@app.route("/")
def home():
    return "Hello, World!"


@app.route("/send_attempt",methods = ['POST'])
def send_attempt():
    try:
        # Get JSON data from the request
        json_data = request.get_json()

        # Extract task ID from the JSON data
        task_id = json_data.get('idT', None)

        if task_id is None:
            raise ValueError("'id' is missing in the JSON data")

        # Check if the task exists in the database
        task = tasks_collection.find_one({"idT": task_id})

        if task is None:

            # If the task doesn't exist, create a new task
            new_task = {
                "idT": task_id,
                "name": json_data.get("name", ""),
                "description": json_data.get("description", ""),
                "attempts": []
            }
            tasks_collection.insert_one(new_task)
            task = new_task
            previous_attempts = []

        else:

            # If the task exists, retrieve previous attempts
            previous_attempts = task.get('attempts', [])[:]

        code =  json_data.get("code", "")
        input = json_data.get("code_input", "")
        output = json_data.get("code_output", "")

        compiled_code = json.loads(grazie_compiler_request(vlada, code, input, output).replace("'", "\""))
        print(f"Compiled code: {compiled_code}")
        if compiled_code["error"] or not compiled_code["valid"]:
            hints = json.loads(grazie_assistant_request(vid, task, code).replace("\"", "").replace("'", "\""))["hints"]

        else:
            hints = json.loads(grazie_assistant_request(vesna, task, code).replace("\"", "").replace("'", "\""))["hints"] \
                    + json.loads(grazie_assistant_request(veles, task, code).replace("\"", "").replace("'", "\""))["hints"] \

        new_attempt = {
            "timestamp": json_data.get("time", ""),
            "hints": hints,
            "code": code,
            "correct": compiled_code["valid"]

        }

        task['attempts'].append(new_attempt)




        #print(task['attempts'])
        #print(task)
        # Update the task in the database
        tasks_collection.update_one({"idT": task_id}, {"$set": task})


        # Prepare response data with both previous and new attempts
        response_data = {"status": "success", "message": "Attempt data inserted into MongoDB",
                         "previous_attempts": previous_attempts, "new_attempt": new_attempt}
        return jsonify(response_data), 200

    except Exception as e:
        # Handle any exceptions that might occur
        error_message = {"status": "error", "message": str(e)}
        return jsonify(error_message), 400

@app.route("/add_weakness", methods = ["POST"])

def add_weakness():
    try:
        json_data = request.get_json()
        new_weakness = {
            "name" : json_data.get("name",""),
            "description": json_data.get("description",""),
            "suggestion":json_data.get("suggestions","")
        }
        weakness_collection.insert_one(new_weakness)

        response_data = {"status": "success", "message": "Everything okay"}
        return jsonify(response_data), 200

    except Exception as e:
        error_message = {"status": "error", "message": str(e)}
        return jsonify(error_message), 400



if __name__ == "__main__":
    app.run( port=8000, debug=True)