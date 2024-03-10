from flask import Flask, jsonify, request
import json
import re
import os

app = Flask(__name__)

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))
# Load the JSON file
with open(os.path.join(current_directory, 'favs.json.txt'), 'r') as file:
    data = json.load(file)

# Endpoint to get all tweets
@app.route('/tweets', methods=['GET'])
def get_all_tweets():
    tweets = [{'created_at': tweet['created_at'], 'id': tweet['id'], 'text': tweet['text']} for tweet in data]
    return jsonify(tweets)

# Endpoint to get all external links grouped by tweet ids
@app.route('/external_links', methods=['GET'])
def get_external_links():
    links = {}
    for tweet in data:
        tweet_id = tweet['id']
        tweet_text = tweet['text']
        extracted_links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet_text)
        links[tweet_id] = extracted_links
    return jsonify(links)

# Endpoint to get details about a specific tweet by its id
@app.route('/tweets/<tweet_id>', methods=['GET'])
def get_tweet(tweet_id):
    for tweet in data:
        if str(tweet['id']) == tweet_id:
            return jsonify({'created_at': tweet['created_at'], 'text': tweet['text'], 'screen_name': tweet['user']['screen_name']})
    return jsonify({'message': 'Tweet not found'}), 404


# Endpoint to get detailed profile information about a specific Twitter user by screen name
@app.route('/user/<string:screen_name>', methods=['GET'])
def get_user_profile(screen_name):
    user = next((tweet['user'] for tweet in data if tweet['user']['screen_name'] == screen_name), None)
    if user:
        profile_info = {'location': user['location'], 'description': user['description'], 'followers_count': user['followers_count'], 'friends_count': user['friends_count']}
        return jsonify(profile_info)
    else:
        return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
