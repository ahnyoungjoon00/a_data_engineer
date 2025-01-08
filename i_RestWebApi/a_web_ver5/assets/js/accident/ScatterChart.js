import { fakeApi } from "./api.js";

export default class ScatterChart {
    // 최고기온과 운량과의 관계
    transformData(datas) {
        //최고기온, 운량
        const tempCloud = datas.map(e => {
            return {
              highTmp:e.high_tmp ,
              avgCloud:e.avg_cloud
            }
        })
        console.log(tempCloud); 
        //레코드별 data를 컬럼별 data로 변경
        const highTemp = {};
        const avgCloud = {};
        tempCloud.forEach((e, key) => {
            highTemp[key] = e.highTmp ;
            avgCloud[key] = e.avgCloud ;
        });

        return [highTemp, avgCloud]
    }

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
      document.querySelector('#chartBox').innerHTML = '';
      return true;
    }
    
    async drawChart() {
      var parent_this = this ;
      this.drawInfo();
      $(document).on('click', '#resBtn', async function(){
        document.querySelector('#option').innerHTML = '';
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
        //console.log(datas);
        const [ //최종 그래프 그릴때 사용할 데이터     
            highTmp, avgCloud
        ] =parent_this.transformData(datas); //현재 클래스 transformData 호출    
    
        parent_this.drawChartFin(highTmp, avgCloud); //그래프 그리기(최초 그래프는 평균기온으로 그림)          
      }) //on끝
    } //drawChart끝

    drawChartFin(highTemp, avgCloud){
      //////////////////////////////////////////////////////////////////////////////
      // 그래프 코드
      // y축 범위 설정위한 변수
      let tmpArr = Object.keys(highTemp).map(item => highTemp[item]);
      let minTmp = Math.min.apply(null,tmpArr)
      let maxTmp=Math.max.apply(null,tmpArr)
      // 무조건 그려지는 시계열 그래프
      var tempCloud = { 
          x: Object.values(avgCloud), //x축 data는 운량
          y: Object.values(highTemp), //y축 data는 최고기온
          type:'scatter',
          mode:'markers',
          marker:{size:12},
      };      


      //////////////////////////////////////////////////////////////////////////
      // layout 구성
      // xticks : x축의 값으로 사용할 data 구성 x축은 운량의 실제값
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
            range:[minTmp-5,maxTmp+5] //기온에 따라 축범위 설정

          }
      };     

      var data = [tempCloud] ;
      Plotly.newPlot('chartBox', data, layout); //newPlot(그래프출력공간, 그래프data, 축data)
    } //drawChartfin()끝

} //class끝