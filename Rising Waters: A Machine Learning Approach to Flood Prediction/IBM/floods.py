import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "7GXqDfQFvfAlblRYWtZz2dDP5BiWvckEphpjhxfFiqTo"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": ['Temp',	'Humidity',	'Cloud Cover',	'ANNUAL',	'Jan-Feb',	'Mar-May',	'Jun-Sep',	'Oct-Dec',	'avgjune',	'sub'], "values": [[ 1.72403408,  0.46694616, -0.09320324, -0.29800606,  0.95764282]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/dc6a7a35-261d-4430-9fdd-3d1a6d4ec7c6/predictions?version=2023-02-11', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
# print(response_scoring.json())
predictions=response_scoring.json()
pred=predictions['predictions'][0]['values'][0][0]
if pred==0:
    print("Flood Predicion= No chance of flood ")
else:
    print("Flood Predicion= Severe chance of flood ")

