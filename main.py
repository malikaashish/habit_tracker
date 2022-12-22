import requests
from datetime import datetime

logo = '''

 _       ____    ____   _  __  ____    _   _   _____      _____  _  _    _   _____
/ \  /| /  _ \  |  __\ / |/ / /  _ \  / \ / \ /__ __\    /__ __\/ \/ \__/ | /  __/
| |  || | / \ | | \/ | |   /  | / \ | | | | |   / \        / \  | || |\/| | |  \  
| |/\|| | \_/ | |    / |   \  | \_/ | | \_/ |   | |        | |  | || |  | | |  /_ 
\_/  \| \____/  |_/\_\ |_|\_\ \____/  \____/    \_/        \_/  \_/\_/  \_| \____\
                                                                     
'''

def log():
    print(logo)

log()
step1 = True

while step1:
    USERNAME = input("Enter your Unique username\n")
    TOKEN = input("Enter your Unique safety token\n")
    # MY_USERNAME = "malikaashish"
    # MY_TOKEN = "hf92btn32fi9238d"

    GRAPH_ID = "graph1"

    pixela_endpoint = f"https://pixe.la/v1/users"

    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response1 = requests.post(url=pixela_endpoint, json=user_params)
    print(response1.text)
    status1 = int(response1.status_code)
    step2 = 200 <= status1 < 300

    while step2:
        graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

        graph_config = {
            "id": GRAPH_ID,
            "name": "Study Graph",
            "unit": "min",
            "type": "float",
            "color": "ajisai"
        }
        headers = {
            "X-USER-TOKEN": TOKEN
        }

        response2 = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
        print(response2.text)
        status2 = int(response2.status_code)
        step3 = 200 <= status2 < 300

        while step3:
            print(f"you can check your progress by following link- {pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}.html")
            pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

            today = datetime.now()

            pixel_data = {
                "date": today.strftime('%Y%m%d'),
                "quantity": input("\nHow many minutes you workout today?\n"),
            }

            response3 = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
            print(response3.text)
            status3 = int(response3.status_code)
            step4 = 200 <= status3 < 300
            while step4:
                step5= int(input("\nDo you want to update or delete your progress? Choose option 1, 2 or"
                                 " 3\n 1. Update\n 2. Delete\n 3. Not needed\n"))
                if step5 == 1:
                    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
                    update_data = {
                        "quantity": "45",
                    }
                    response = requests.put(url=update_endpoint, json=update_data, headers=headers)
                    print(response.text)
                elif step5 == 2:
                    delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

                    response = requests.delete(url=delete_endpoint, headers=headers)
                    print(response.text)
                else:
                    step4 = False