\# Week 11 실습

\## 오늘 한 것

* PyInstaller 설치 및 빌드
* resource\_path() 함수 추가
* \--add-data 옵션으로 에셋 포함
* .exe 실행 확인

\## resource\_path() 를 써야 하는 이유

* exe빌드 후에도 파일 경로가 정상적으로 동작함.
* 개발 중과 빌드 후 코드를 동일하게 사용할 수 있음.
* 이미지, 음악, 폰트 관련 오류를 줄일 수 있음.
* 다른 컴퓨터나 운영체제에서도 실행 가능성을 높일 수 있음.
* 프로젝트 구조를 체계적으로 관리할 수 있음.



\## 빌드 명령어

* pyinstaller: 가장 기본적인 exe 생성 명령어
* \--onefile: 실행 파일 하나로 압축하여 생성
* \--windowed: 콘솔창(cmd 창) 숨김
* \--add-data: 이미지, 음악, 폰트 같은 추가 파일 포함
* "assets;assets": assets 폴더를 exe 내부에도 assets 이름으로 포함
* \--name=MyGame: 생성될 exe 파일 이름 지정



\## AI 활용 내역

* PyInstaller를 사용한 exe 빌드 방법 학습
* resource\_path() 함수 사용 이유 및 적용 방법 학습
* os.path.join()을 사용한 상대 경로 수정 방법 학습
* \--add-data 옵션을 이용한 assets 폴더 포함 방법 학습
* 이미지, 음악, 폰트 파일 경로 오류 해결
* SyntaxError, TypeError 등 빌드 과정에서 발생한 오류 해결
* exe 빌드 후 정상 실행 여부 확인 방법 학습

