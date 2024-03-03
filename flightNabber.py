import requests

## Information to connect to API
url = "https://test.api.amadeus.com/v1/security/oauth2/token"
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
}
data = 'grant_type=client_credentials&client_id=jiQSp1zIpDPANrGmk2pztvoejteaL3jH&client_secret=iIw4mflqR7hYXN1F'

## Connects with API, returns access token
payload = requests.post(url, headers=headers, data=data)
print(payload.text)

## Grabs the access token from the payload. Payload must be accessed as JSON object to retrieve access token
if payload.status_code == 200:
  access_token = payload.json().get('access_token')
  print(access_token)

  ## Lets try and grab flight data from the API (SEARCHING WITH PARAMETERS!!!!!!)
  urlFLIGHTS = "https://test.api.amadeus.com/v2/shopping/flight-offers"
  headersFLIGHTS = {
    'Authorization': f'Bearer {access_token}'
  }
  paramsFLIGHTS = {
    "originLocationCode": "LGA",
    "destinationLocationCode": "CLT",
    "departureDate": "2024-03-05",
    "adults": 1
  }

  res = requests.get(urlFLIGHTS, headers=headersFLIGHTS, params=paramsFLIGHTS)
  print(res.text)
else: 
  print("ERROR: ", payload.status_code)
