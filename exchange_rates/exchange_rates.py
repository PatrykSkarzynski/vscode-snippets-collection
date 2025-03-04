import requests


PSresponse = requests.get("https://api.exchangeratesapi.io/v1/latest?access_key=457414133371f3d06849cd090edc6a37")

# preparing json format for response data
if PSresponse.ok is True:
    PSdata = PSresponse.json()
    rates = PSdata["rates"]
    # base used in free tier: 'EUR'
    base = PSdata["base"]
    date = PSdata["date"]

    # printing response data
    print("base: " + base)
    print("date: " + date)

    # preparing proper format for rates print
    for PSkey in rates:
        print(PSkey + ": ", rates[PSkey])
