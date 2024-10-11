import requests

def classify_job(description):
    url = 'https://tabiya-api.com/classify'
    try:
        response = requests.post(url, json={'description': description})

        # Check if the request was successful
        response.raise_for_status()  # Raises an error for bad responses (4xx, 5xx)

        # Return the JSON response
        return response.json()
    
    except requests.exceptions.RequestException as e:
        # Handle errors (network issues, invalid responses, etc.)
        print(f"An error occurred: {e}")
        return {'error': str(e)}  # Return an error message in JSON format
