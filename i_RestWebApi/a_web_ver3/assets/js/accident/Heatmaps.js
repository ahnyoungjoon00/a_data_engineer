import {fakeApi} from './api.js'

export default class Heatmaps{

    transformData(datas){
        // 요일별 낮/밤 별 사망자 부상자 수
        // 날짜 => 요일, 낮/밤, 사망자수, 부상자수
        let accidents = datas.map(e => {
            // 날짜 : yyyyMMdd
            const year = e.date.substring(0,4);
            const month = e.date.substring(4,6);
            const date = e.date.substring(6,8);

            const occurDate = new Date(year, month - 1, date);
            const week = occurDate.getDay();

            return {
                week: week,
                dayOrNight: e.dayOrNight,
                deathCnt: e.deathCnt,
                injuryCnt: e.injuryCnt
            }
        });

        const dayOrNights = Map.groupBy(accidents, ({dayOrNight}) => dayOrNight);
        const dayWeek = Map.groupBy(dayOrNights.get('day'), ({week}) => week);
        const nightWeek = Map.groupBy(dayOrNights.get('night'), ({week}) => week);
        const dayWeekSum = [];
        const nightWeekSum = [];

        console.dir(dayWeek);

        dayWeek.keys().forEach(key => {
            console.dir(dayWeek.get(key).length)
            let sum = dayWeek.get(key)
            .reduce((acc, cur) => {
                return acc += cur.deathCnt
            }, 0);

            dayWeekSum.push(sum);
        });

        nightWeek.keys().forEach(key => {
            let sum = nightWeek.get(key)
            .reduce((acc, cur) => {
                return acc += cur.deathCnt
            }, 0);

            nightWeekSum.push(sum);
        })

        return [dayWeekSum, nightWeekSum]
    }

    async drawChart(){
        document.querySelector('#chartBox').innerHTML = '';
        const datas = await fakeApi();
        const [dayWeekSum, nightWeekSum]  = this.transformData(datas)

        var data = [
            {
              z: [dayWeekSum, nightWeekSum],
              x: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
              y: ['낮', '밤'],
              type: 'heatmap',
              hoverongaps: false
            }
          ];

          Plotly.newPlot('chartBox', data);
    }

}