from flask import Flask,request, jsonify
from db import Connection


app = Flask(__name__)
db = Connection("codding_tasks_db")
tasks_collection = db.tasks
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
                "attempts": [],
                "solution":"1,2,3"
            }
            tasks_collection.insert_one(new_task)
            task = new_task
            previous_attempts = []

        else:

            # If the task exists, retrieve previous attempts
            previous_attempts = task.get('attempts', [])[:]

        # Add the new attempt to the task's attempts array
        new_attempt = {
            "timestamp": json_data.get("time", ""),
            "code": json_data.get("code", ""),
            "hint":"asd",
            "correct":"True"

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


if __name__ == "__main__":
    app.run( port=8000, debug=True)