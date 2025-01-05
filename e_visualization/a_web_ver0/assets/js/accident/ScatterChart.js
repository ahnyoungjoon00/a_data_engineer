import { fakeApi } from "./api.js";

export default class ScatterChart {
    transformData(datas) {
        // 일별 사망/부상자 건수를 scatter chart로 작성
        const dateAccidents = datas.map(e => {
            const date = e.date.substring(4,6) + '/' + e.date.substring(6,8);
            return {
                date: date,
                deathCnt : e.deathCnt,
                injuryCnt: e.injuryCnt,
            }
        })

        const grouped = Map.groupBy(dateAccidents, ({date}) => date);
        const dateDeath = {}
        const dateInjury = {}
        grouped.forEach((e, key) => {
            dateDeath[key] = e.reduce((acc, cur) => acc + cur.deathCnt, 0);
            dateInjury[key]  = e.reduce((acc, cur) => acc + cur.injuryCnt, 0);
        });

        // console.dir(dateDeath)

        return [dateDeath, dateInjury]
    }

    async drawChart() {
        document.querySelector('#chartBox').innerHTML = '';
        const datas = await fakeApi();
        const [
            datehDeath, dateInjury
        ] =this.transformData(datas);

        var trace1 = {
            x: Object.keys(datehDeath),
            y: Object.values(datehDeath),
            type: 'scatter',
            mode:"markers",
            marker:{size:12},
          };
          
        //   var trace2 = {
        //     x: Object.keys(dateInjury),
        //     y: Object.values(dateInjury),
        //     type: 'scatter',
        //     mode:"markers",
        //   };

          var layout = {
            title: {text: 'scatter Chart'},
            width: 1000,
            height: 500,
            xaxis:{
                title:{
                    text:"사망"
                }            
            },
            yaxis:{
                title:{
                    text:"부상"
                }            
            },
          };
          
          var data = [trace1, trace2];
          Plotly.newPlot('chartBox', data, layout);
    }
}