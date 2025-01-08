import { fakeApi } from "./api.js";

export default class ScatterChart {
    // 최고기온과 운량의 관계
    transformData(datas) {
        // 최고기온, 운량
        const tempCloud = datas.map(e => {
            return {
                highTmp : e.high_tmp,
                avgCloud: e.avg_cloud,
            }
        })
        // 레코드별 data를 컬럼별 data로 변경 
        const highTmp = {};
        const avgCloud = {};

        tempCloud.forEach((e, key) => {
          highTmp[key] = e.high_tmp;
          avgCloud[key]  = e.avgCloud;
        });

        return [highTmp, avgCloud]
    };

    drawInfo(){
      document.querySelector('#addInfo').innerHTML = '';
      document.querySelector('#option').innerHTML = '';
      const str = `
      <select id='year' class="form-select form-select-lg mb-3" aria-label=".form-select-lg example">
            <option selected>년도선택</option>
            <option value="1">2023</option>
            <option value="2">2024</option>
            <option value="3">2023 vs 2024</option>
      </select>        
      `
      $('#addInfo').append(str);
      const str2 = `
      <select id='month' class="form-select form-select-lg mb-3" aria-label=".form-select-lg example">
            <option selected>월 선택</option>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
            <option value="6">6</option>
            <option value="7">7</option>
            <option value="8">8</option>
            <option value="9">9</option>
            <option value="10">10</option>
            <option value="11">11</option>
            <option value="12">12</option>
      </select>        
      ` 
      $('#addInfo').append(str2);
      const str3 = '<input type="button" id="resBtn" value="Result">'
      $('#addInfo').append(str3);
      document.querySelector('#chartBox').innerHTML = ''; //그래프영역 지우기
      return true;
    };
    
    async drawChart() {
      var parent_this = this;
      this.drawInfo();
      $(document).on('click', '#resBtn', async function(){
        document.querySelector('#option').innerHTML = ''; // 안해도 되는데, 경우에 따라서 남아있을수도 있어서 다시 한번
        let mode = $('#year').val(); //선택된 연도에 해당되는 value가 반환(1~3) ->클래스 속성에 저장
        let month = $('#month').val();//선택된 월의 value 반환(1~12)
        let url = "";
        if(mode=='1'){
            url="http://127.0.0.1:8000/api/weather/2023/"+month+"/";
        }else if (mode=="2"){
            url="http://127.0.0.1:8000/api/weather/2024/"+month+"/";
        }else {
            url="http://127.0.0.1:8000/api/weather/"+month+"/";
        }           

        const datas = await fakeApi(url); //api data 요청(비동기방식요청 async ~ await)
        // console.log(datas);
        const [
          highTmp, avgCloud
        ] =parent_this.transformData(datas);
        // [ //최종 그래프 그릴때 사용할 데이터이고 여러 함수에서 사용해야 함(클래스 속성 - 데이터 재 요청시까지 보존)        
        //     parent_this.date, parent_this.year, parent_this.avgTmp, parent_this.lowTmp, parent_this.highTmp, parent_this.cloudData
        // ]  //현재 클래스 transformData 호출    
    
        parent_this.drawChartFin(highTmp, avgCloud); //그래프 그리기(최초 그래프는 평균기온으로 그림)  
      }) // on 끝
    } // drawChart 끝

    drawChartFin(highTmp, avgCloud){
      //////////////////////////////////////////////////////////////////////////////
      // 그래프 코드
      // 기온(y)축 범위 설정 변수
      let tmpArr = Object.keys(highTmp).map(item => highTmp[item]);
      let minTmp = Math.min.apply(null,tmpArr)
      let maxTmp=Math.max.apply(null,tmpArr)
      // 무조건 그려지는 시계열 그래프
      var tempCloud = { 
          x: Object.values(avgCloud),
          y: Object.values(highTmp),
          type:"scatter",
          mode:"markers",
          marker:{size:12},
      };

      //////////////////////////////////////////////////////////////////////////
      // layout 구성
      // xticks : x축의 값으로 사용할 data 구성 x축은 날짜를 의미
      let val = Object.keys(date[0]).map(Number); //수치형값 0~59
      let text = Object.values(date[0]);
      console.log(val);
      console.log(text)

      var title=""
      if(mode=="3"){
        title="월별 기온 변화";
      }else if (mode=="2"){
       // console.log(year);
        title=year[0][0]+"년 월별 기온 변화";
      }else {
        title=year[0][0]+"년 월별 기온 변화";
      }

      var layout = {
        title: {text: '일별 최고기온과 평균운량과의 관계'},
        width: 800,
        height: 500,
        xaxis: {
            title: {
              text: '운량'
            },
            showline:true,
            dtick:1,
            range:[0,12]
          },
          yaxis: {
            title: {
              text: '최고기온'
            },
            ticklen:5,
            range:[minTmp-5,maxTmp+5]
          }
      };
      
      var data = [tempCloud];
      Plotly.newPlot('chartBox', data, layout);
    }
  } // class 끝