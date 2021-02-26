## 딥러닝 전력예측 웹시스템(09.10~ing)   
  ### 따릉이 데이터 분석  
   - [datastudy_bicycle](https://github.com/Jimin980921/DeepLearning_websys/blob/master/datastudy_bicycle.ipynb)  
      - 데이터: __[공공자전거 이용정보](http://data.seoul.go.kr/dataList/OA-15245/F/1/datasetView.do)__   
      (출처:서울열린데이터광장)  
      
      -  [x] 시간대별 대여건수,반납건수 분석해보기  
      > 출근시간과 퇴근시간대에 자전거 대여, 반납건수가 많음  
      <img src="https://user-images.githubusercontent.com/57060127/95681212-91841400-0c19-11eb-9b68-81457d68d4ed.JPG" width=50%>
      <br>
      
   --------------------------------------------------------------------------------------------
   ### 전력 데이터 분석   
   - [data_task1](https://github.com/Jimin980921/DeepLearning_websys/blob/master/data_task1.ipynb)  
      - 데이터: __전력이용 1,7월 데이터(비공개)__    
     
      -  [x] 1월, 7월 데이터 월별, 일별, 시간별(15분단위) 분석해보기  
      __일(day)별__  
      > 1월보다는 7월이 전체적으로 사용량이 많음  
      <img src="https://user-images.githubusercontent.com/57060127/95681081-d8bdd500-0c18-11eb-9380-a979057b6a34.JPG" width=50%>  
      
      __시간(15분)별__   
      > 1월과 7월모두 아침 9시와 저녁 6시에 전력사용량 peak  
      > 새벽시간대보다 출근시간~퇴근시간대에 전력사용량이 많음   
      <img src="https://user-images.githubusercontent.com/57060127/95681080-d78ca800-0c18-11eb-8af6-cc74253fc09d.JPG" width=50%>  
      <br>
      
   - [data_task2](https://github.com/Jimin980921/DeepLearning_websys/blob/master/data_task2.ipynb)   
      -  [x] 요일별 분석해보기  
      > 일요일의 전력사용량이 상대적으로 낮은것으로보아 휴일에 전력사용량이 낮음  
      <img src="https://user-images.githubusercontent.com/57060127/95680939-0f472000-0c18-11eb-809c-296266b96c87.JPG" width=50%>
      <br>
      
   - [LSTM(ver.2)](https://github.com/Jimin980921/DeepLearning_websys/blob/master/data_task2.ipynb)  
      - 데이터: __전력이용 1,7월 데이터(비공개)__   
      
      -  [x] LSTM 분석   
      -  [x] LSTM 파라미터변경  
      -  [x] 온도요인추가하기  
      -  [x] 전력요인으로만 예측한것vs전력+온도요인예측 정확도 비교  
      
      i) optimizer= adam  
       __전력만__ 평균 오차율= 0.06  
       __전력+온도__ 평균 오차율= 0.46  
   
      ii) optimizer= RMSProp   
       __전력만__ 평균 오차율= 2.73  
       __전력+온도__ 평균 오차율= 3.33  
      > 전력만 사용했을때가 전력+온도를 함께 사용했을때보다 정확도가 높은 것을 알 수 있음  
      <br>
      
   - [LSTM(ver.4)](https://github.com/Jimin980921/DeepLearning_websys/blob/master/LSTM(ver.4).ipynb)  
      - 데이터: __전력이용 1년 데이터(비공개)__   
      
      -  [x] 전력요인으로만 예측한것vs전력+온도요인예측 정확도 비교  
      
      __전력만__ 평균절대비오차= 3.04   
      <img src="https://user-images.githubusercontent.com/57060127/102181907-b2edce80-3eee-11eb-8781-33fabfafb7b1.JPG" width=50%>
      
      __전력+온도__ 평균절대비오차= 4.54  
      <img src="https://user-images.githubusercontent.com/57060127/102181902-b1bca180-3eee-11eb-8704-5619780ad346.JPG" width=50%>
      
      > 전력만 사용했을때가 전력+온도를 함께 사용했을때보다 정확도 높은 것을 확인  
      <br>
      
   - [CNN+LSTM 하이브리드모델](https://github.com/Jimin980921/DeepLearning_websys/blob/master/CNN%2BLSTM(per_season).ipynb)  
      - 데이터: __전력이용 1년 데이터(비공개)__  
      
      -  [x] 계절성 모델  
      
-  봄  
 
__전력(2.97)__            |  __전력+온도(2.96)__
:-------------------------:|:-------------------------:
![](https://user-images.githubusercontent.com/57060127/109316509-0b4a3080-788f-11eb-8188-6926bc517e62.png){: width="100" height="100"}  |  ![](https://user-images.githubusercontent.com/57060127/109316610-26b53b80-788f-11eb-9d55-35ffe772056e.png){: width="100" height="100"}  

-  여름  
__전력(17.57)__            |  __전력+온도(17.34)__
:-------------------------:|:-------------------------:
![](https://user-images.githubusercontent.com/57060127/109317213-d2f72200-788f-11eb-9c90-db827e178b8b.png){: width="100" height="100"}  |  ![](https://user-images.githubusercontent.com/57060127/109317251-de4a4d80-788f-11eb-9c5c-8915f6c9b163.png){: width="100" height="100"}  

-  가을 
__전력(5.03)__            |  __전력+온도(5.05)__
:-------------------------:|:-------------------------:
![](https://user-images.githubusercontent.com/57060127/109317509-1fdaf880-7890-11eb-85f2-932f02c47633.png){: width="100" height="100"}  |  ![](https://user-images.githubusercontent.com/57060127/109317550-29646080-7890-11eb-9602-9b788518d5b3.png){: width="100" height="100"}  

-  겨울
__전력(5.86)__            |  __전력+온도(6.32)__
:-------------------------:|:-------------------------:
![](https://user-images.githubusercontent.com/57060127/109317633-41d47b00-7890-11eb-8d59-9ca40ab5b0c9.png){: width="100" height="100"}  |  ![](https://user-images.githubusercontent.com/57060127/109317678-4ac54c80-7890-11eb-85ec-2a97c78160ec.png){: width="100" height="100"}  


-  [LSTM 최종모델](https://github.com/Jimin980921/DeepLearning_websys/blob/master/LSTM(per_season).ipynb)  
      - 데이터: __전력이용 1년 데이터(비공개)__  
      
      -  [x] 계절성 모델   
      > 전력만 사용했을때가 전력+온도를 함께 사용했을때보다 정확도 높은 것을 확인  
      <br>
      
   - 조건별 모델
    -  [X] 계절별(3-6월:봄, 6-8월:여름, 9-11월:가을, 12-2월:겨울)  
    -  [X] 요일별 예측모델 
    -  [X] 모델 합치기  
      <br>
      <br>
      
      ---------------------------------------------------------------------------------------------------------------
      ### Web개발실습  
   - Flask   
   설치: pip install flask (flask 웹 프레임워크 사용)    
   __anaconda prompt 관리자모드 -> 경로이동__   
      - app.py  
         python app.py 실행  
      - routing.py  
         python routing.py 실행  
   <br> 
   

  
   
   
   
   
   
  
   
  
      
  
  
