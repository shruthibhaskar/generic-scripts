import requests

# Set variables
endpoint = "health-check-endpoint"
slack_webhook_url = "https://hooks.slack.com/services/dummy/dummy"
channel = "#alert-test"
botname = "Health Check Bot"

# Function to send message to Slack
def send_slack_message(message):
    payload = {
        "channel": channel,
        "username": botname,
        "text": message
    }
    requests.post(slack_webhook_url, json=payload)

# Print initial message with formatting
print("-----------------------------")
print("Initiating health check for the ednpoint...")
print("-----------------------------")

try:
    # Perform GET request with a timeout of 60 seconds
    response = requests.get(endpoint, timeout=60)
    status_code = response.status_code

    # Check the response status and send detailed messages
    if status_code == 200:
        print("-----------------------------------------")
        print("Health check completed for ednpoint.\nStatus code: {}".format(status_code))
        print("-----------------------------------------")
        send_slack_message("🟢 The endpoint is up and running. Status code: {}")
    else:
        print("-----------------------------------------")
        print("Health check completed for endpoint.\nStatus code: {}".format(status_code))
        print("-----------------------------------------")
        send_slack_message("🔴 The endpoint is not returning 200. Status code: {}")

except requests.RequestException as e:
    print("-----------------------------")
    print("Failed to reach the endpoint.")
    print("-----------------------------")
    send_slack_message("❗ Failed to reach the endpoint")
