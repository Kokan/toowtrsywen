import requests

url = "http://127.0.0.1:8000/check_in_out/check_in_out/"
name = input("Dolgozó neve:")
in_or_out = input("Belépés vagy kilépés('in'/'out'/'ho'):")
myobj = { "name_text": name, "in_or_out": in_or_out}
x = requests.post(url,data=myobj)
print(x.text)