

























































































import  requests

def main():
    base = input("First Currency: ")
    other = input("Second Currency: ")

    res = requests.get("http://data.fixer.io/api/latest?access_key=ead9ad7a802879a2973d3a45582b40a2",
                        params={"from": base, "to": other, "amount": 1})
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    rate = data["rates"][other]
    print(f"1 {base} is equal to {rate} {other}")

if __name__ == "__main__":
    main()