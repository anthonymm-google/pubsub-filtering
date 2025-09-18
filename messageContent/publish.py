from google.cloud import pubsub_v1
import json
import argparse

def publish_message(project_id: str, topic_name: str, asset_id: int, device_id: int, build_id: int):
    """Publishes a message to a Pub/Sub topic with the given asset_id, device_id, and build_id."""
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)

    message_data = {
        "asset_id": asset_id,
        "device_id": device_id,
        "build_id": build_id
    }
    data = json.dumps(message_data).encode("utf-8")

    future = publisher.publish(topic_path, data)
    print(f"Published message ID: {future.result()}")

if __name__ == "__main__":
    project_id = "amm-demo"  # Replace with your Google Cloud project ID
    topic_name = "testing"  # Replace with your Pub/Sub topic name
    
    parser = argparse.ArgumentParser(description="Publish a message to a Pub/Sub topic.")
    parser.add_argument("--asset_id", type=int, required=True, help="The asset ID for the message.")
    parser.add_argument("--device_id", type=int, required=True, help="The device ID for the message.")
    parser.add_argument("--build_id", type=int, required=True, help="The build ID for the message.")

    args = parser.parse_args()

    publish_message(
        project_id,
        topic_name,
        asset_id=args.asset_id,
        device_id=args.device_id,
        build_id=args.build_id,
    )

# Example usage:  python publish.py --asset_id=5 --device_id=5 --build_id=5