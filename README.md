# RECOOK

> #### Welcome to π [Recook](http://j4a204.p.ssafy.io/) π
> size : Responsive(387 x 858)


<br>

## Project Summary π§­

μ¬λ£ κΈ°λ° λ μνΌ μΆμ² μλΉμ€

##### πΈ μ μ λ°°κ²½

- μ½λ‘λ19λ‘ μΈν μΈμ κ°μ, μ§μμ μλ¦¬νλ νμ μ¦κ°
- μ§μμ μλ¦¬λ₯Ό νλ μ¬λλ€μ΄ μ¦κ°νλ©΄μ λ μνΌμ νμμ± μ¦κ°

##### πΈ μλΉμ€ μ»¨μ

- μ νν μ¬λ£λ‘ λ§λ€ μ μλ μλ¦¬ λ μνΌλ₯Ό μΆμ²ν΄μ£Όλ μλΉμ€
- μ¬λ£μ λ§λ λ μνΌλ₯Ό μΌμΌμ΄ μ°Ύμλ΄μΌ νλ λΆνΈν¨ ν΄μ

##### πΈ νκ²

- μ§μμ λ¨μ μ¬λ£λ‘ λ§μλ μλ¦¬λ₯Ό λ§λ€μ΄ λ¨Ήκ³  μΆμ μ¬λ

##### πΈ κΈ°κ°

- Feb 22th 2021 ~ Apr 9th 2021

##### πΈ κ²°κ³Όλ¬Ό

- [Architecture & Usecase_Diagram](./document/Architecture.md)
- [Sequance_Diagram](./document/SequanceDiagram.md)
- [PPT](./document/νΉνPJT_μ΅μ’λ°ν_A204_μ΅μ’.pdf)
- [UCC](https://www.youtube.com/watch?v=snwMDh_cxQE)





<br>

## Project Info :pushpin:

### Usage π

#### π» Front-end

- Vue.js

  - Project Setup

    ```bash
    $ npm install 
    ```

  - Compiles and hot-reloads for development

    ```bash
    $ npm run serve
    ```

  - Compiles and minifies for production

    ```bash
    $ npm run build
    ```

  - Run your tests

    ```bash
    $ npm run test
    ```

  - Lints and fixes files

    ```bash
    $ npm run lint
    ```

- Customize configuration

  - [Configuration Reference](https://cli.vuejs.org/config/)

#### π» Back-end

**Install**

- Java (Open JDK 14)

- Maven

- STS 

- Mariadb

  - create tables

    run dump.sql => [dump.sql](./document/dump.sql)

- Django

  - Project Setup

    ```bash
    $ pip3 install -r requirements.txt
    # μ€λ₯λλ λͺ¨λμ μλμΌλ‘ κΉμμ£ΌμΈμ
    ```

  - DB Connection

    ```bash
    $ python manage.py inspectdb
    ```
  
  - migration
  
    ``` bash
    $ python manage.py makemigrations
    ```
  
  - Run
  
    ```bash
    $ python manage.py runserver
    ```

<br>



### Tech Stack π§©

- Backend : Spring Boot, Django, MariaDB
- Frontend : Vue.js

![κΈ°μ μ€ν](https://user-images.githubusercontent.com/44192706/114414148-88d0c280-9be9-11eb-81fc-7e78a52d2cda.png)



### Database Modeling :link:

![erd](https://user-images.githubusercontent.com/44192706/114414118-83737800-9be9-11eb-8775-31c19557f6f2.png)



<br>



### Features :sparkles:

##### 	π λ©μΈ κΈ°λ₯

```
- μ μ μ μ·¨ν₯(μμμ’λ₯, μλ λ₯΄κΈ°)μ λΆμνκΈ° μν μ€λ¬Έμ‘°μ¬
- μ¬λ£λ₯Ό μ ννλ©΄ λ§λ€ μ μλ λ μνΌ μΆμ²
- μ¬μ©μμ μ·¨ν₯(μμμ’λ₯, μλ λ₯΄κΈ°)μ λΆμν κ°μΈ λ§μΆ€ν λ μνΌ μΆμ²
- κ° λ μνΌ λ§λ€ λΉμ·ν μ¬λ£λ₯Ό κ°μ§κ³  λ§λ€ μ μλ μ°κ΄ λ μνΌ μ κ³΅
```

##### 	π λΆκ° κΈ°λ₯

```
- ν΄λΉ λ μνΌμ ν¬ν¨λ μ μ μ μλ λ₯΄κΈ° μ λ³΄ μλ¦Ό
- λ μνΌλ₯Ό μ°ν΄ λκ³  λͺ¨μλ³Ό μ μλ κΈ°λ₯
- μ΅κ·Όμ λ³Έ λ μνΌ νμΈ κ°λ₯
- ν΄λΉ λ μνΌλ₯Ό λ³΄κ³  μ μ κ° λ§λ  μμ μ¬μ§ κ²μ κΈ°λ₯
- νμ μ λ€μ΄ κ²μν μμ μ¬μ§ λͺ¨μλ³΄κΈ° κΈ°λ₯
- μμ κ΄λ ¨ μμ μ κ³΅
```

##### 	π μ¬μ©ν λΉλ°μ΄ν° μΆμ² μκ³ λ¦¬μ¦
- νμ νν°λ§ Collaborative Filtering
- μ»¨νμΈ  κΈ°λ° νν°λ§ Content based Filtering

<br>



### Pages in Detail :mag:

> κ° νμ΄μ§ λ³ μκ°

- ##### Survey

![μ·¨ν₯μ‘°μ¬](https://user-images.githubusercontent.com/44192706/114414258-9dad5600-9be9-11eb-8b6f-48521b41580e.gif)
- ##### Main

![λ©μΈ](https://user-images.githubusercontent.com/44192706/114416291-7ce60000-9beb-11eb-84b6-7bfdecbaa730.gif)

  

- ##### Recipe Detail

![λ μνΌμμΈ](https://user-images.githubusercontent.com/44192706/114416286-7bb4d300-9beb-11eb-8bdf-2db68c61fbab.gif)
  
  

- ##### Review

![λ¦¬λ·°λͺ¨μλ³΄κΈ°](https://user-images.githubusercontent.com/44192706/114414313-ab62db80-9be9-11eb-8019-762e2296be97.gif)

  

- ##### MyPage(My Review & Like)

![λ¦¬λ·°μ°](https://user-images.githubusercontent.com/44192706/114414299-a867eb00-9be9-11eb-8483-eb01fcb10267.gif)

  

- ##### Cook Video

![μ νλΈ](https://user-images.githubusercontent.com/44192706/114414281-a1d97380-9be9-11eb-83a2-5bcbe01ea55c.gif)

### Recipe Source π

- [ν΄λ¨Ήλ¨λ](https://haemukja.com/)

#### μ¬μ©λ λ°μ΄ν° μμ€λ [haemukja.com](https://haemukja.com/) μ¬μ΄νΈμμ λ³΄μ΄λ λ μνΌ μ λ³΄(μ΄λ―Έμ§, μ¬λ£λ¦¬μ€νΈ, νκ·Έ, μ‘°λ¦¬λ²)κ° μμ ν¬λ‘€λ§ν λ°μ΄ν°λ‘ μμμ  λͺ©μ μ΄ μλ κ΅μ‘μ  λͺ©μ μΌλ‘λ§ μ¬μ©λμμμ μλ €λλ¦½λλ€.



