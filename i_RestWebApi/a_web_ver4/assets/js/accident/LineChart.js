import { fakeApi } from "./api.js";

export default class LineChart {
    constructor(){ //클래스 속성 : 데이터 재요청 전까지 기존 data 보존
        let date=null;
        let year=null;
        let lowTmp=null;
        let highTmp=null;
        let avgTmp=null;
        let cloudData=null;
        let mode=null; // drawChart()에서 실제 그래프 그리는 코드는 따로 분리해서 함수로 구성(인수로 사용할 변수)
        }

    transformData(datas) {
        // 날짜, 평균기온, 운량
        const data = datas.map(e => {
            const date = e.date.substring(5,10) ; //월-일만 추출(x축 tick 라벨로 사용)
            const year = e.date.substring(0,4); //groupby 및 범례, 그래프 제목에 활용
            return {
                date: date,
                year: year,
                lowTmp:e.low_tmp,
                highTmp:e.high_tmp,
                avgTmp : e.avg_tmp,
                avgCloud: e.avg_cloud,
            }
        })//map 함수 종료

        //mode가 3이어서 2023/2024 data가 반환된 경우 연도별 groupby 해야 연도별 비교가 가능
        const grouped = Map.groupBy(data,({year})=>year) ; //년도별로 groupby 진행, 연도가 1개일 경우에는 group이 1개만 생김
        console.log(grouped); //map 객체 -> array 객체로 변경해야 함
        let yearArray=[];
        let i = 0  ;
        for (let key of grouped.keys()){
            yearArray[i]=grouped.get(key);
            i=i+1;
        }
        console.log(yearArray);

        //레코드로 반환된 데이터를 컬럼 data로 변환
        //그룹데이터를 array로 변환했고, 두개 이상 연도가 있을 수 있으므로 연도별로 작업해야 함    
        //연도별 최종 data를 저장할 빈 배열 변수 생성
        let yearfin=[];
        let datefin=[];
        let avgTmpfin=[];
        let lowTmpfin=[];
        let highTmpfin=[];
        let cloudDatafin=[];

        for(let j=0; j<yearArray.length; j++){
        const date = {};
        const year= {};
        const avgTmp = {};
        const highTmp = {};
        const lowTmp = {};
        const cloudData = {};
        yearArray[j].forEach((e, key) => { //api data 각각 접근해서 data 분리
            date[key] = e.date;
            avgTmp[key]  = e.avgTmp;
            cloudData[key] = e.avgCloud;
            highTmp[key] = e.highTmp;
            lowTmp[key] = e.lowTmp;
            year[key] = e.year;
        });//foreach끝
        //1개년도의 컬럼 data를 최종 배열 변수에 추가
        datefin[j]=date;
        yearfin[j]=year;
        avgTmpfin[j]=avgTmp;
        lowTmpfin[j]=lowTmp;
        highTmpfin[j]=highTmp;
        cloudDatafin[j]=cloudData;
        }//for끝
        console.log(datefin);
        return [datefin, yearfin, avgTmpfin, lowTmpfin, highTmpfin,cloudDatafin]
    }

    drawInfo(){
        document.querySelector('#addInfo').innerHTML = '';
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
      }

    drawInfo2(){
        document.querySelector('#option').innerHTML = '';
        const str = `
        <select id='temp' class="form-select form-select-lg mb-3" aria-label=".form-select-lg example">
              <option value="1" selected>평균기온</option>
              <option value="2">최고기온</option>
              <option value="3">최저기온</option>
        </select>        
        `
        $('#option').append(str);
        return true;
      }
      
    async drawChart() {    
        var parent_this = this; //클래스를 지칭하는  this참조값을 변수에 저장
        this.drawInfo(); //연/월 선택할 수 있는 select box 추가(현재 클래스 메서드(this:클래스))
        $(document).on('click', '#resBtn', async function(){
            //this.drawInfo2(); //기온종류 선택 select box 추가(this:drawChart)
            parent_this.drawInfo2();
            parent_this.mode = $('#year').val(); //선택된 연도에 해당되는 value가 반환(1~3) ->클래스 속성에 저장
            let month = $('#month').val();//선택된 월의 value 반환(1~12)
            let url = "";
            if(parent_this.mode=='1'){
                url="http://127.0.0.1:8000/api/weather/2023/"+month+"/";
            }else if (parent_this.mode=="2"){
                url="http://127.0.0.1:8000/api/weather/2024/"+month+"/";
            }else {
                url="http://127.0.0.1:8000/api/weather/"+month+"/";
            }           

            const datas = await fakeApi(url); //api data 요청(비동기방식요청 async ~ await)
            console.log(datas);
            [ //최종 그래프 그릴때 사용할 데이터이고 여러 함수에서 사용해야 함(클래스 속성 - 데이터 재 요청시까지 보존)        
                parent_this.date, parent_this.year, parent_this.avgTmp, parent_this.lowTmp, parent_this.highTmp, parent_this.cloudData
            ] =parent_this.transformData(datas); //현재 클래스 transformData 호출    
        
            parent_this.drawChartFin(parent_this.date, parent_this.year,parent_this.avgTmp,parent_this.mode); //그래프 그리기(최초 그래프는 평균기온으로 그림)  

    }) //resultbtn on 끝

    $(document).on('change', '#temp', function(){
      let mode = $('#temp').val(); //현재 선택된 기온종류의 value
      if (mode=="1"){ //평균기온선택
          parent_this.drawChartFin(parent_this.date, parent_this.year,parent_this.avgTmp,parent_this.mode);
      } else if (mode=="2"){ //최고기온선택
          parent_this.drawChartFin(parent_this.date, parent_this.year,parent_this.highTmp,parent_this.mode);
      } else { //최저기온선택
          parent_this.drawChartFin(parent_this.date, parent_this.year,parent_this.lowTmp,parent_this.mode);
      }
    });//기온종류선택
    } //drawChart 끝

    drawChartFin(date, year, tmpData, mode){
        //////////////////////////////////////////////////////////////////////////////
        // 그래프 코드
        
        // 무조건 그려지는 시계열 그래프
        var temp = { 
            x: Object.keys(tmpData[0]), //x축 data는 tmpData의 key값(0~n)
            y: Object.values(tmpData[0]), //y축 data는 평균기온
            mode: "lines+markers", //표식이 있는 시계열 그래프
            line: {
                dash:'dot',
                width:2,
                color:'red',
                shape:'spline' //부드러운 곡선
            },
            name:'기온('+year[0][0]+')', //범례용
        };
        
        if(mode == '3') { //2023 vs 2024일 경우
        var temp1 = { 
            x: Object.keys(tmpData[1]), //x축 data는 tmpData의 key값(0~n)
            y: Object.values(tmpData[1]), //y축 data는 기온
            mode: "lines+markers", //표식이 있는 시계열 그래프
            line: {
                dash:'dot',
                width:2,
                color:'blue',
                shape:'spline' //부드러운 곡선
            },
            name:'기온('+year[1][0]+')', //범례용
        };
        } //if 끝

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
            title: {
              text:title,
              font: {
                family: 'Courier New, monospace',
                size: 24
              },
              xref: 'paper',
              x: 0.5,
            }, //title 끝
            xaxis: {
              title: {
                text: 'date',
                font: {
                  family: 'Courier New, monospace',
                  size: 18,
                  color: 'black'
                }
              },
              showline:true,
              showgrid:false,
              gridcolor:'#dcdcdc',
              ticklen:5,
              dtick:1,
              ticktext:text, //초기값 1 선이 나오면 움직이면 됨
              tickvals:val    
            }, //x축 끝
            yaxis: {
              title: {
                text: '기온의 변화',
                font: {
                  family: 'Courier New, monospace',
                  size: 18,
                  color: 'black'
                }
              },
              showline:false,
              showgrid:true,
              gridcolor:'#dcdcdc',
              tickformat: ",.0f",
              ticklen:5,
              griddash:'dot',
              range:[-5,40]
            } //y축 끝
        }; //layout 끝  
        
        if(mode=='3'){
        var data = [temp, temp1];
        } else {
            var data = [temp] ;
        }
        Plotly.newPlot('chartBox', data, layout); //newPlot(그래프출력공간, 그래프data, 축data)
    } //drawChartfin()끝
}//class 끝