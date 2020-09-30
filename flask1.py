# 사전에 cmd에서 pip install flask

from flask import Flask

app = Flask(__name__)
# Flask라는 객체를 생성하고 인자로 __name__
# 단일 모듈 사용시 __name__을 인자로 써야함
# 앱이 시작되는지 혹은 모듈로 임포트 되는지에 따라 이름이 달라지기 때문
# 패키지를 사용한다면 인자로 패기지 이름을 넣음(플라스크에서 템플릿이나 정적 파일을 찾을 때 필요)

@app.route('/')
# route() 데코레이터로 Flask에게 어떤 URL이 우리가 작성한 함수를 실행시키는지 알려준다. 
# 데코레이터(Decorator):하나의 함수를 취해서 또 다른 함수를 반환하는 함수
def hello_world():
    with open("test.html", "r", encoding="utf-8") as f:
        a = f.read()
    return a
    # return 뒤에는 브라우저에 전송될 메시지

if __name__ == '__main__':
    app.run()
    # 로컬 서버로 실행.
    # __name__=='__main__'은 이 서버가 현재 동작중인 유일한 서버라는 뜻
    # 가상 머신을 사용하고 있다면 app.run(host="0.0.0.0")으로 외부에서 접속이 가능하다고 함

# 아무 폴더에나 이런 파일을 만들고 실행시키면 서버가 열리는게 신기하다.
# node.js와 궤를 같이 한다고 들었다. node.js가 더 찾기 쉽고 사용자가 많아서 더 건드리진 않을 것 같다..
# 거의 리눅스 기반으로 사용하고 강의도 거의 다 리눅스기반.
