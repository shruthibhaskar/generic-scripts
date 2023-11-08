#!/bin/bash

# Set variables
endpoint="<health_check_endpoint_url>"
slack_webhook_url="https://hooks.slack.com/services/<slack_web_hook_of_your_channel>"
channel="#alert-test" # Channel name
botname="Health Check Bot"

# Function to send message to Slack
send_slack_message() {
    local message="$1"
    curl -X POST -H 'Content-type: application/json' --data "{
        \"channel\": \"$channel\",
        \"username\":\"$botname\",
        \"text\": \"$message\"
    }" "$slack_webhook_url"
}

# Print initial message with formatting
echo "-----------------------------"
echo "Initiating health check for the stg intranet proxy..."
echo "-----------------------------"

# Perform curl request with error handling and timeout
response=$(curl -s -o /dev/null -w "%{http_code}" -m 60 "$endpoint" 2>/dev/null)

# Check the response status and send detailed messages
if [ $? -eq 0 ]; then
    if [ $response -eq 200 ]; then
        echo "-----------------------------------------"
        echo "Health check completed for stg intranet proxy."
        echo "Status code: $response"
        echo "-----------------------------------------"
        send_slack_message "🟢 The endpoint is healthy. Status code: $response."
    else
        echo "-----------------------------------------"
        echo "Health check completed for stg intranet proxy."
        echo "Status code: $response"
        echo "-----------------------------------------"
        send_slack_message "🔴 The endpoint is unhealthy. Status code: $response."
    fi
else
    echo "-----------------------------"
    echo "Failed to reach the stg intranet proxy."
    echo "-----------------------------"
    send_slack_message "❗ Failed to reach the $endpoint."
fi
