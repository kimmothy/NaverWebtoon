# NaverWebtoon
이 리퍼지토리는 2019년 1학기 "Human Computer Interaction" 수업에서의 팀 프로젝트에 쓰인 웹 크롤링과 이미지 분석 코드입니다.

NaWebCrolling.py는 가장 먼저 실행해볼 코드입니다.
이 코드는 네이버 웹툰에 등록된 현재 연재작과, 완결웹툰의 제목, 별점, 장르 정보를 수집하고, 섬네일 이미지를 저장합니다.
수집한 데이터와 이미지는 C:\python_data\webtoon에 저장됩니다.

ClusterByRGBHist는 섬네일 이미지에 쓰인 RGB 세가지 요소의 빈도를 바탕으로 이미지를 클러스터링합니다. 
이 분석에 쓰인 RGB 히스토그램의 모양은 HistSample.py를 사용해 볼 수 있습니다.

ClusterByColors&Lines는 선의양 그리고 서로 구분되는 색이 얼마나 쓰였는가를 바탕으로 섬네일 이미지를 클러스터링합니다.
