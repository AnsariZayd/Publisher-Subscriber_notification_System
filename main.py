from flask import Flask, request, jsonify

app = Flask(__name__)

# Data structures to hold topics and subscribers
subscriptions = {}


@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.json
    topic_id = data['topicId']
    subscriber_id = data['subscriberId']

    if topic_id not in subscriptions:
        subscriptions[topic_id] = set()

    subscriptions[topic_id].add(subscriber_id)
    return jsonify({"message": f"Subscriber {subscriber_id} subscribed to {topic_id}"}), 200


@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    topic_id = data['topicId']

    if topic_id in subscriptions:
        subscribers = list(subscriptions[topic_id])
        return jsonify({"message": f"Notification sent to subscribers of {topic_id}", "subscribers": subscribers}), 200
    else:
        return jsonify({"error": "Topic not found"}), 404


@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    data = request.json
    topic_id = data['topicId']
    subscriber_id = data['subscriberId']

    if topic_id in subscriptions and subscriber_id in subscriptions[topic_id]:
        subscriptions[topic_id].remove(subscriber_id)
        return jsonify({"message": f"Subscriber {subscriber_id} unsubscribed from {topic_id}"}), 200
    else:
        return jsonify({"error": "Subscription not found"}), 404


@app.route('/subscriptions', methods=['GET'])
def get_subscriptions():
    # Convert sets to lists for JSON serialization
    serializable_subscriptions = {topic: list(subs) for topic, subs in subscriptions.items()}
    return jsonify(serializable_subscriptions), 200


if __name__ == '__main__':
    app.run(debug=True)
