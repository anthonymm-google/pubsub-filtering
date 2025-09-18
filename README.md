# Pub/Sub Subscriber Message Filtering

This document outlines two approaches for a Google Cloud Pub/Sub subscriber to filter incoming messages and only process those that meet specific criteria.

## Summary

When building a Pub/Sub subscriber, it's common to only be interested in a subset of messages published to a topic. Instead of processing every message, you can filter them and only acknowledge (ACK) the ones that are relevant. This prevents unwanted messages from being processed and, if they are not acknowledged, allows them to be redelivered to other subscribers.

1.  **Message Content Filtering**: Inspecting the body (`data`) of the message to decide whether to process it.  This approach can impact throughput and latency as message sizes grow.

2.  **Custom Attribute Filtering**: Inspecting the message metadata (`attributes`) to make a processing decision. Also enables subscription filtering on the custom attribute values.

## Message Content Filtering
`messageContent/publish.py`- publishes a message to a topic

`messageContent/receive_FilterMessageContent.py`- receives messages from a subscription and only ACK's messages for a specific attribute in the body of the message

### Message Attribute Filtering
`customAttribute/publish_CustomAttribute.py`- publishes a message to a topic with a custom attribute

`customAttribute/receive_FilterCustomAttribute.py`- receives messages from a subscription and only ACK's messages for a specific custom attribute value