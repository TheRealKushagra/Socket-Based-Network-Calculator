from flask import Flask, render_template, request
from client import send_request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None
    input_value = ""
    selected_operation = "subnet"

    if request.method == "POST":
        selected_operation = request.form.get("operation", "subnet")
        input_value = request.form.get("input_value", "").strip()

        if not input_value:
            error = "Please enter an IP address or network CIDR."

        else:
            if selected_operation == "subnet":
                payload = {
                    "operation": "subnet",
                    "ip": input_value
                }

            elif selected_operation == "ip_class":
                payload = {
                    "operation": "ip_class",
                    "ip": input_value
                }

            elif selected_operation == "range":
                payload = {
                    "operation": "range",
                    "cidr": input_value
                }

            else:
                payload = None
                error = "Invalid operation selected."

            if payload:
                response = send_request(payload)

                if response.get("success"):
                    result = response["result"]
                else:
                    error = response.get(
                        "error",
                        "Something went wrong while processing the request."
                    )

    return render_template(
        "index.html",
        result=result,
        error=error,
        input_value=input_value,
        selected_operation=selected_operation
    )


if __name__ == "__main__":
    print("Starting Flask Network Calculator...")
    print("Open http://127.0.0.1:5000 in your browser.")

    app.run(host="127.0.0.1", port=5000, debug=True)