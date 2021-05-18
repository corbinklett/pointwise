import requests as req

resp = req.get("http://0.0.0.0:5000")

print(resp.text)