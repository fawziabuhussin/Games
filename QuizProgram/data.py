import requests

# The generated data are from open Trivia: https://opentdb.com/api_config.php.
# Used https://www.freeformatter.com/html-escape.html way to unformat the HTML.
# If you wish you can add more paramters such as Category (after '?' mark) 18 is for CS questions!

params = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean", params=params)
response.raise_for_status()
question_data = response.json()["results"]