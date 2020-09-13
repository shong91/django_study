모델(model)
 - 웹 서비스에서 사용할 특성 등을 정의한 내용. 
 - 저장, 처리하기 원하는 정보들을 구조화, 개념화한 것. 
 - schema 
 
데이터베이스(database)
 - 저장 공간 (system)
 - 모델링된 스키마의 정보를 따르는 테이블들의 집합
 - RDMS, NoSQL, ... 
 
 ex 맛집
 1) 종류(정보): 맛집, 평가, 회원, ... 
 2) 속성: 
    1 - 맛집: 주소, 명칭, 평가 
    2 - 평가: 별점, 리뷰, 회원(작성자) 등 
    3 - 회원: 닉네임, 이메일 등
 3) 자료형: str, int, ref(point, relation)
 4) 릴레이션 정의: 1 <- 2 <- 3 은 상호 연관됨 .. (ex 2 - 회원(작성자)는 3을 참조함)
 
 
```
        저장
 DB    <=====>    webApp
        읽기

상기 프로세스를 통일성있게 테이블에 연결되도록 자동으로 처리해주는 것이 Django Model의 역할. 
```




MVC pattern             MTV pattern
Model                   Model (model.py)
View                    Template (templates/*)
Controller              View (views.py)


Request                 Response

client                  server

Process
1) request (url GET)
2) request 받음
3) url conf
4) url mapping view 결정 (urls.py)
5) execute method (views.py) 
6) render => html
7) response


##
ORM(Object-Relational Mapping)
하나의 클래스가 실제 자료구조에 연동된다. ?
(모델클래스)    (DB스키마)

##
릴레이션(Relation)
Article <=======> User
1) Many to Many
2) Many to One
3) One to One

조인(Join) 


