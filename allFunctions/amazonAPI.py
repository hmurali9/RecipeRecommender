import requests
import json


def apicall():
    url = "https://www.amazon.com/afx/ingredients/landing"
    querystring = {"tag": "yuminc-21"}

    # Sample hardcoded set of ingredients
    # Refer ../documents/*API-Documentation* for more information
    ingredients = {"ingredients": [
        {
            "name": "red apples",
            "componentIndex": 0,
            "quantityList": [
                {
                    "unit": "COUNT",
                    "amount": 5
                },
                {
                    "unit": "KILOGRAMS",
                    "amount": 0.5
                }
            ],
            "exclusiveOverride": False
        },
        {
            "name": "strawberry non-fat greek yogurt",
            "brand": "chobani",
            "asinOverrides": [
                "B002GVJZI4"
            ],
            "componentIndex": 0,
            "quantityList": [
                {
                    "unit": "OUNCES",
                    "amount": 5
                }
            ],
            "exclusiveOverride": False
        }
    ]
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.mealbutlers.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15',
        'Referer': 'https://www.mealbutlers.com',
    }

    response = requests.request('POST', url, data={"ingredients": json.dumps(ingredients, ensure_ascii=False)},
                                headers=headers, params=querystring)

    for line in response.text.split("\n"):
        if line.find("data-encoded-recipe-url") >= 0:
            final_url = 'https://www.amazon.com' + line.split("'")[1]

    return final_url
