# Twitter Archive REST API

This project implements a set of REST APIs to retrieve information from a Twitter archive JSON file. The APIs are built using Flask, a lightweight web framework for Python.

## Installation

1. Clone the repository or download the python script from the repository:
   
     git clone https://github.com/kadercoder/376assignment2.git

2. Keep a Twitter archive JSON file in the same directory. This repo already has one name favs.json.

3. Run the Flask application:
   
    python assignment2.py

## Usage

You can use tools like Postman to send HTTP requests to the provided endpoints and retrieve the desired information.

## Endpoints

### Get all tweets

Returns a JSON object containing all tweets available in the archive.

- **URL**: `/tweets`
- **Method**: `GET`

### Get all external links

Returns a JSON object containing external links grouped by tweet ids.

- **URL**: `/external_links`
- **Method**: `GET`

### Get details about a specific tweet by its id

Returns a JSON object containing details about a specific tweet identified by its id.

- **URL**: `/tweets/<tweet_id>`
- **Method**: `GET`
- **Parameters**:
  - `tweet_id`: The id of the tweet

### Get detailed profile information about a specific Twitter user by screen name

Returns a JSON object containing detailed profile information about a specific Twitter user identified by their screen name.

- **URL**: `/user/<screen_name>`
- **Method**: `GET`
- **Parameters**:
  - `screen_name`: The screen name of the user

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or improvements, please open an issue or submit a pull request.

