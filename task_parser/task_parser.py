import csv

import requests

from workers.celery_worker import celery_app


@celery_app.task(name="task_parser")
def task_parser():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    response.raise_for_status()
    users = response.json()

    field_names = ["id", "name", "email"]

    with open("../users.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()

        for user in users:
            user_data = {
                "id": str(user["id"]),
                "name": user["name"],
                "email": user["email"],
            }
            writer.writerow(user_data)

    num_users = len(users)

    return f"Saved {num_users} users to users.csv"
