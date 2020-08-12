import requests


class Versions:
    def __init__(self):
        # self.url = "http://localhost:8000/api/versions"
        self.url = "https://icarussoftlandings.com/api/versions"
        self.headers = {"Content-Type": "application/x-www-form-urlencoded"}

    def post(self):
        payload = f"username=icarus" f"&password=tarbaby0"
        url_payload = f"{self.url}?{payload}"
        requests.request("POST", url_payload, headers=self.headers)


def main():
    updater = Versions()
    updater.post()


if __name__ == "__main__":
    main()

