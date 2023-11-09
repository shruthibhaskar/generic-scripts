import requests

# Set variables
endpoint = "http://10.40.76.4:3128"
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
print("Initiating health check for the stg intranet proxy...")
print("-----------------------------")

try:
    # Perform GET request with a timeout of 60 seconds
    response = requests.get(endpoint, timeout=60)
    status_code = response.status_code

    # Check the response status and send detailed messages
    if status_code == 200:
        print("-----------------------------------------")
        print("Health check completed for stg intranet proxy.\nStatus code: {}".format(status_code))
        print("-----------------------------------------")
        send_slack_message("🟢 The stg intranet proxy is up and running. Status code: {}. Augustine, please review the script and provide feedback if necessary.".format(status_code))
    else:
        print("-----------------------------------------")
        print("Health check completed for stg intranet proxy.\nStatus code: {}".format(status_code))
        print("-----------------------------------------")
        send_slack_message("🔴 The stg intranet proxy is not returning 200. Status code: {}. Augustine, please review the script and provide feedback if necessary.".format(status_code))

except requests.RequestException as e:
    print("-----------------------------")
    print("Failed to reach the stg intranet proxy.")
    print("-----------------------------")
    send_slack_message("❗ Failed to reach the stg intranet proxy. Augustine, please review the script and provide feedback if necessary.")
