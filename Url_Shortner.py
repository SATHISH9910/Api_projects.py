import requests

BASE_URL = "https://tinyurl.com/api-create.php"

Long_url = input("Enter Your url to shorten: ")

try:
    response=requests.get(BASE_URL,{"url":Long_url},timeout=5)
    
    response.raise_for_status()

    short_url=response.text

    print("\n====URl Shortner====")
    print("original url:",Long_url)
    print("short url:",short_url)

except response.exceptions.ConnectionError:
    print("NO internet connection")
except response.exceptions.Timeout:
    print("Request timed out")
except response.exception.HTTPError:
    print("Server returns an error")
except Exception as e:
    print("Error :",e)