from google.cloud import pubsub_v1
import json
import argparse

def receive_messages_with_device_id(project_id: str, subscription_name: str, device_id: str):
    """Receives messages from a Pub/Sub subscription and acknowledges only those
    with a matching 'device_id' attribute."""

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

        ack_ids = []
        for received_message in response.received_messages:
            message_data = json.loads(received_message.message.data.decode('utf-8'))
            
            if str(message_data.get("device_id")) == device_id:
                print(f"Received and acknowledging message with device_id {device_id}: {received_message.message.data.decode('utf-8')}")
                ack_ids.append(received_message.ack_id)
            else:
                print(f"Received message with device_id {message_data.get('device_id')}, not acknowledging.")
        if ack_ids:
            subscriber.acknowledge(request={"subscription": subscription_path, "ack_ids": ack_ids})

if __name__ == "__main__":
    project_id = "amm-demo"  # Replace with your Google Cloud project ID
    subscription_name = "testing-sub"  # Replace with your Pub/Sub subscription name

    parser = argparse.ArgumentParser(description="Retreive messages from a Pub/Sub subscription and filter by device_id.")
    parser.add_argument("--device_id", type=str, required=True, help="The device_id to acknowledge.")
    args = parser.parse_args()

    receive_messages_with_device_id(project_id, subscription_name, args.device_id)

# Example usage:  python receive_FilterMessageContent.py --device_id=5