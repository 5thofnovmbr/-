> requests 모듈
```python
import requests as req
# req이라는 이름으로 requests 모듈을 불러온다.
```
> 주로 쓰는 두 가지 방법
```python
res = req.get(url, params=parmas, cookies=cookies)
# get은 params를 인자로 받는다.(파라미터)

res = req.post(url, data=data, cookies=cookies)
# post는 data를 인자로 받는다.
# files도 인자로 받아서 파일을 보낼 수도 있다.(검색ㄱㄱ)
```
> parmas, data, cookies는 딕셔너리 형태로 입력받는다.
```python
# 딕셔너리 자료형
d = {"key1":"value1", "key2":"value2"}
```
> 예시
```python
url = "주소"

pr = {
	"id":"admin",
	"pw":"000000"
}

dt = {
	"id":"admin"
}

ck = {
	"PHPSESSID":"ddddd"
}

with req.get(url, params=pr, cookies=ck) as res:
	print(res.text)
	# res.text로 그 페이지의 정보를 받아올 수 있다.

# res는 responce 줄임말
# req.get()에 바로 입력해도 무관.
# ex) req.get("http://~", params={"id":"admin", "pw":"pwpwpw"}, cookies={"PHPSESSID":"dfdfdfefdf"})
# url끝에 ~.php?id=admin or 1=1-- 처럼 바로 쓰고 params를 추가하지 않아도 괜찮다.

# 다른 코딩방법
res = req.get(url, params=pr, cookies=ck)
print(res.text)
```
```
url에 &은 %26, #은 %23으로 써야하는데 파이썬으로 보낼 때는 그냥 &, #으로 쓰면 된다.
```