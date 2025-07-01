## **Docker란?**
    - 리눅스 컨테이너 기반으로하는 오픈소스 가상화 플랫폼이다.
    **컨테이너란**
        - 애플리케이션과 그 실행에 필요한 모든 것을 하나로 묶어, 어디서나 동일하게 실행될 수 있도록 해주는 독립된 실행 환경입니다.
---
## **Docker 구성요소**
    1. Docker Engine
        Docker의 핵심 실행 시스템으로, 컨테이너를 생성하고 관리하는 데 사용되는 클라이언트-서버 구조의 플랫폼입니다.
    2. Docker Image
        컨테이너 실행에 필요한 모든 파일과 설정이 포함된 불변의 템플릿입니다.
    3. Docker Container
        이미지를 기반으로 실행되는 독립된 애플리케이션 실행 환경입니다.
    4. Dockerfile
        이미지를 자동으로 생성하기 위한 설정 파일로, 이미지 빌드 과정을 코드로 정의합니다.
    5. Docker Hub (또는 Registry)
        Docker 이미지의 저장소로, 이미지를 업로드하거나 다운로드할 수 있는 중앙 저장 공간입니다.
---
## **Docker Image와 Docker Container**
    - **Docker Image**
        - 애플리케이션과 그 실행에 필요한 모든 파일과 설정을 포함하는 불변의 템플릿입니다.
        - 이미지는 실행 가능한 상태로, 컨테이너를 생성하는 데 사용됩니다.
        -  실행 전 상태의 ‘설계도’라 생각 할 수 있습니다.
    - **Docker Container**
        - 이미지를 기반으로 실행되는 독립된 애플리케이션 실행 환경입니다.
        - 컨테이너는 이미지의 인스턴스로, 실행 중인 프로세스와 그 상태를 포함합니다.
        - 컨테이너는 격리된 환경에서 실행되며, 다른 컨테이너와 독립적으로 동작합니다.
        - 이미지의 ‘실행된 실체’ 라 생각 할 수 있습니다.
---
## **CI/CD와 Github Actions**
    - **CI(Continuous Integration)**
        - 지속적인 통합이라는 의미로, 작업한 코드를 주기적으로 빌드 및 테스트하여 레포지토리에 통합(merge)하는 것이다.
        - CI 자동화 : 파일을 작업 후 오랜 기간이 지나고 통합하면 코드들의 충돌이 발생할 수 있다. 이 때문에 CI 자동화를 통해
          변경되거나 추가되는 코드들을 자동으로 검수할 수 있는 Build Test를 진행해 코드의 충돌을 방지한다.
    - **CD(Continuous Delivery & Continuous Deployment)
        - 지속적인 서비스 제공 및 지속적인 배포를 의미한다.
        - 코드 변경 사항의 병합부터 프로덕션에 적합한 빌드 제공에 이르는 모든 단계로, 테스트 자동화와 코드 배포 자동화가 포함된다
          완료된 빌드를 코드 리포지토리에 자동으로 배포할 수 있기 때문에 운영팀이 보다 빠르고 손쉽게 애플리케이션을 프로덕션으로 배포할 수 있게 된다.
---
## **PostgreSQL의 장점**
    - 무료 오픈소스 : PostgreSQL 은PostgreSQL라이센스를 가지고 있어서 자유롭게 이용할 수 있을뿐더러 품질과 기능 개선이 빠르게 돌아간다.
    - 안전성 : 트랜잭션과 장애 복구 기능이 기본으로 탑재되어 있어, 외부 도구 없이도 높은 신뢰성을 유지할 수 있다.
    - 확장성 : 다양한 데이터 타입과 확장 기능을 지원하여, 복잡한 데이터 모델링이 가능한다.
    - 성능 : 자동 인덱싱, 병렬 쿼리 처리, 캐시 최적화 등으로 대용량 데이터 처리 시에도 일관된 성능을 제공한하며,
            고급 SQL 기능과 JSON, 배열, 사용자 정의 타입 등 다양한 데이터 구조를 지원해, 여러 용도를 하나의 시스템에서 처리할 수 있습니다.
---
## **1) Project Settings**
#### **Model 구조**
    - 1) User => users
    - email
    - password
    - nickname
    - is_business

    - 2) Video => videos
    - title
    - description
    - link
    - views_count
    - video_file
    
    - 3) Reaction => reactions
    - User : FK
    - Video : FK
    - reaction (like, dislike, cancel)

    - 4) Comment => comments
    - User : FK
    - Video : FK    
    - content
    - like
    - dislike

    - 5) Subscription => subscriptions
    - User : FK => subscriber
    - User : FK => subscribed_user

    - 6) Common => common
    - created_at
    - updated_at