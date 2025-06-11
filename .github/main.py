from google.cloud import pubsub_v1
import json

def process_file(event, context):
    file_info = {
        "name": event["name"],
        "size": event["size"],
        "format": event["contentType"]
    }

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path("your-project-id", "file-upload-topic")
    publisher.publish(topic_path, json.dumps(file_info).encode("utf-8"))
