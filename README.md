# unistclub
club web application for unist people

# Account
## 회원가입
    * URL:  ~/account/signup -> "`{% url 'account:signup_url' %}"`
    * HTML:  /registration/signup.html
    * view: "`def signup(request):"`
    ### form 사용
        * django 제공 UserCreationForm 상속.
## 회원가입 완료
    * URL:  ~/account/signup_ok -> "`{% url 'account:signup_ok_url' %}"`
    * HTML:  /registration/signup_ok.html
## 로그인
    * URL:  ~/account/login -> "`{% url 'account:login_url' %}"`
    * HTML:  /registration/login.html (아직 미연결)
    ### form 사용
        * django 제공 login form 그대로 사용.

## 로그아웃
    * URL:  ~/account/logout -> "`{% url 'account:logout_url' %}"`
    * HTML:  redirect를 login.html

# Club
