import requests
import json
import base64
def api_request(urs, pwd):
    # First Endpoint
    endpoint1 = 'https://isms.iaa.ac.tz/ismsapi/hakiki.php'

    # Username and password
    username = 'bcsClass'
    password = 'jaribuKuingia@bcs$$+++!XZty'

    # Prepare the POST data
    data1 = {
        'username': username,
        'password': password,
    }

    # Send the request
    response = requests.post(endpoint1, json=data1, verify=False)

    # Check for errors
    if response.status_code != 200:
        raise requests.RequestException(f'Error: {response.status_code}')

    # Parse the response
    data = response.json()

    # Retrieve the token from the response
    token = data.get('token')

    # Validate the token
    if token is None:
        raise ValueError('Failed to retrieve token')

    # Second Endpoint
    endpoint2 = "https://isms.iaa.ac.tz/ismsapi/ca.php"

    login_username = urs
    login_password = pwd

    # Set the authentication headers
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json"
    }

    data2 = {
        'username': login_username,
        'password': login_password,
    }

    # Send the request
    response = requests.post(endpoint2, headers=headers, json=data2, verify=False)

    # Check for errors
    if response.status_code != 200:
        raise requests.RequestException(f'Error: {response.status_code}')

    # Parse the response
    data = response.json()

    if 'error' in data:
        raise ValueError('Invalid User')
    else:
        records = json.loads(base64.b64decode(base64.b64decode(data)).decode('utf-8'))

    # Process the response or return it as needed
    # return JsonResponse(records)
    return records
