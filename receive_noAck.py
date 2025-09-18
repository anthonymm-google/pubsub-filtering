from google.cloud import pubsub_v1
import time

def receive_messages(project_id: str, subscription_name: str):
    """Receives messages from a Pub/Sub subscription."""

    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, subscription_name)
    
    NUM_MESSAGES = 100 # Default and max is 1,000.  Change as needed.

    with subscriber:
        response = subscriber.pull(
            request={"subscription": subscription_path, "max_messages": NUM_MESSAGES}
        )

        if not response.received_messages:
            print("No messages received.")
            return

        for received_message in response.received_messages:
            print(f"Received message: {received_message.message.data.decode('utf-8')}")

if __name__ == "__main__":
    project_id = "amm-demo"  # Replace with your Google Cloud project ID
    subscription_name = "testing-sub"  # Replace with your Pub/Sub subscription name

    receive_messages(project_id, subscription_name)
