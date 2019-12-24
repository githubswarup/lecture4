import  requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?access_key=ead9ad7a802879a2973d3a45582b40a2&format=1")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    print(data)

if __name__ == "__main__":
    main()