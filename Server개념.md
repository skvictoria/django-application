## Web(World Wide Web)
- 인터넷이라는 네트워크 체계 위에서 동작하는 통신 규약 중 하나

## Static Page vs. Dynamic Page(Database)

## CGI Protocol vs. Application Server 방식
> CGI Protocol
  - 웹 클라이언트 <-> 웹서버(Apache)
  
> Application Server 방식(ASP, JSP)
  - 웹 클라이언트(Browser) <-> 웹서버(Apache, Nginx) <-> 웹 어플리케이션 서버(WAS) <-> DB
  - 웹서버의 역할
    - Proxy
    - HTTP/HTTPS Control
    - Caching
    - Accessing Control
    - Authentication
    - Response Static Page

## HTTP 의 특징
- Connectionless
- Stateless(이전 내용을 기억하고 있지 않음)
- Header : Method(Get방식, Post방식)

## Web Framework
- Back-end
  - Spring(JAVA) - 전자정부 프레임워크 기반, 국내 활용도 높음
  - Django(Python)
      - GUI 관리자 페이지 기본제공
      - 개발 및 유지보수 장점
      - 무료 오픈소스 Web Application Framework
      - MTV model
        - Model (Data Handling) - DB와 ORM(Object Relational Mapping)
        - Template (Static, Dynamic HTML page)
        - View (Service Logic) - template에 rendering, Model CRUD
  - NodeJS(JS) - FrontEnd랑 같은 언어, 가벼움
  
- Front-end
  - Angular(JS) - google이 개발
  - React(JS) - Facebook, Instagram
  - Vue JS(JS) - 최근에 나옴
  
## URL(Uniform Resource Location)
- 프로토콜 - 호스트명 - 포트번호 - 경로 - 쿼리스트링 - 프래그먼트
- http://www.example.com:80/main/services?category=2&kind=devices#n10

