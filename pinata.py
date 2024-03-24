import requests

def api_hit(url):

    url = url
    #dummy key
    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiJiZTJiNjM3ZC04NTRmLTQyYmEtYTFmMC0yNWM5YTAxMWI1ZmQiLCJlbWFpbCI6Im1hbmlkaWxsczQxQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwaW5fcG9saWN5Ijp7InJlZ2lvbnMiOlt7ImlkIjoiRlJBMSIsImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxfSx7ImlkIjoiTllDMSIsImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxfV0sInZlcnNpb24iOjF9LCJtZmFfZW5hYmxlZCI6ZmFsc2UsInN0YXR1cyI6IkFDVElWRSJ9LCJhdXRoZW50aWNhdGlvblR5cGUiOiJzY29wZWRLZXkiLCJzY29wZWRLZXlLZXkiOiIxYzUzM2U0OTBkMTlmZjVhZmQzYiIsInNjb3BlZEtleVNlY3JldCI6IjA5NjM0YWM0NjkyYTUwYzUzZGM2ZGVkZmU0ZGU0YzBmYzliODcwNzkxNjUxMWZlY2U0NmQxMDg3YmI3NWQyMDEiLCJpYXQiOjE3MTEwNTExODB9.hip0CcmHeyUSkX1hKd8MSaWSyyr3dCIK2vcS5BeRUn0"}

    response = requests.request("GET", url, headers=headers)

    return(response.json())


url_1 = f"https://api.pinata.cloud/v3/farcaster/casts/{hash}"
url_2 = f"https://api.pinata.cloud/v3/farcaster/casts"
url_3 = f"https://api.pinata.cloud/v3/farcaster/channels"
url_4 = f"https://api.pinata.cloud/v3/farcaster/channels/{name}"
url_5 = f"https://api.pinata.cloud/v3/farcaster/users/{fid}"
url_6 = f"https://api.pinata.cloud/v3/farcaster/users"
