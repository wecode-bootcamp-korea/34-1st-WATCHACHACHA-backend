# Watcha Classic (위코드 34기 1차 프로젝트)
- 기존의 [왓챠피디아 사이트](https://pedia.watcha.com/ko-KR)는 영화를 비롯한 TV 프로그램, 책, 웹툰에 대한 정보를 조회, 평가, 검색 등의 기능이 구현된 SNS 백과사전 사이트입니다.
- 저희 팀(왓챠챠챠)이 기획한 Watcha Classic은 SNS 기능을 활용한 클래식 영화 백과사전 사이트 왓챠클래식(Watcha Classic)입니다.
<img width="860" alt="Screen Shot 2022-07-03 at 12 57 30 PM" src="https://user-images.githubusercontent.com/102043891/177023992-a4d897ca-cc20-44aa-ba27-2f427ce72707.png">
<br>
TEAM : WATCHACHACHA
<br>
PROJECT : Watcha Classic
<br>
<br>

## 🎙 설명

위의 레포지토리는 [위코드 부트캠프](https://github.com/wecode-bootcamp-korea)의 [34기 백엔드 1차 프로젝트](https://github.com/wecode-bootcamp-korea/34-1st-WATCHACHACHA-backend)입니다.

- [Watcha Classic 백엔드 GitHub 링크](https://github.com/wecode-bootcamp-korea/34-1st-WATCHACHACHA-backend)
- [Watcha Classic 프론트엔드 GitHub 링크](https://github.com/wecode-bootcamp-korea/34-1st-WATCHACHACHA-frontend)

## 📆 개발 기간
- 개발 기간 : 2022-06-20 ~ 2022-07-01 (11일)

## 🧑🏻‍💻 팀 인원
- 총 5명
- Backend : 이태권(PM), 박민하
- Frontend: 김민석, 김은경, 이현범 

## 🖥 Backend 역할

**[이태권(PM)](https://github.com/dev-taekwonlee)**
- dbdiagram을 이용한 모델링 (중심)
- ERD를 실제 model에 적용
- csv file to MySQL (보조)
- token decorator 구현
- 메인 페이지(FilmView) API 구현(GET)
- 프로필 페이지(UserView) API 구현(GET)
- 보고 싶어요(WatchListView) API 구현(GET, POST, DELETE)

**[박민하](https://github.com/miracle-21)**
- dbdiagram을 이용한 데이터 모델링 (보조)
- csv file to MySQL (중심)
- 회원가입(SignupView) API 구현(POST)
- 로그인(SigninView) API 구현(POST)
- 로그인/회원가입 유효성 검사
- 상세 페이지(FilmDetailView) API 구현(GET)

## 💻 Backend 기술 스택

|                                                Language                                                |                                                Framwork                                                |                                               Database                                               |                                                     ENV                                                      |                                                   HTTP                                                   |
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=black"> | <img src="https://img.shields.io/badge/miniconda3-44A833?style=for-the-badge&logo=anaconda&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> |

<br>
<br>

## ❓ 프로젝트 선정 이유
왓챠피디아를 평소에도 자주 활용하고 있어서 해당 사이트의 기능을 직접 기획, 제작해보고 싶었습니다.

<br>
<br>

## 📚 팀 프로젝트 자료

### ERD

![watcha_classic_modeling_20220623](https://user-images.githubusercontent.com/102043891/177026614-1eabbc1b-711b-4d43-a908-e88c12935d1f.png)

### 사이트 시현 사진
<img width="643" alt="Screen Shot 2022-07-01 at 3 59 11 PM" src="https://user-images.githubusercontent.com/102043891/176841574-5d68d365-7687-4a9e-85e7-c83464240429.png">

### 사이트 시현 영상
[데모 영상](https://www.youtube.com/watch?v=AqXCkm3HQTg)

<br>
<br>

## 🛠 협업 툴

### Slack
<img width="942" alt="스크린샷 2022-07-01 오후 3 48 13" src="https://user-images.githubusercontent.com/50426259/176840075-30907e6a-8be6-4914-88d3-fe0d3742ad9c.png">

- 팀원들과의 자료 공유 및 개인적 소통

### Notion
![image](https://user-images.githubusercontent.com/50426259/176840968-aab75ef3-4a5c-4497-a532-db539a297b58.png)
- 매일 진행되는 stand-up meeting에서 각자의 진행 상황과 Blocker 파악 및 소통

### Trello
![trello](https://user-images.githubusercontent.com/50426259/176840626-5bc5b445-4c0b-4259-93bd-56d9f63f2485.gif)
- stand-up meeting을 마친 후 각자 Trello에 반영하여 작업 현황을 일목요연하게 공유

<br>
<br>

## 🔖 Reference
- 이 프로젝트는 [왓챠피디아](https://pedia.watcha.com/) 사이트를 참조하여 학습 목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습 용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
- 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
