import requests


API_URL = "http://127.0.0.1:8000/predict"


reviews = [
    "غذا خیلی خوشمزه بود و خیلی سریع به دستم رسید",
    "غذا سرد بود و اصلا کیفیت خوبی نداشت",
    "پیک افتضاح بود و یک ساعت بعد سفارش را آورد",
    "خیلی راضی بودم ممنون از شما",
    "غذا خوب بود ولی خیلی دیر رسید",
]


for i, review in enumerate(reviews, start=1):

    response = requests.post(
        API_URL,
        json={"text": review}
    )

    print(f"Example {i}")
    print("Review:", review)
    print("Status code:", response.status_code)
    print("Response:", response.json())
    print("-" * 70)