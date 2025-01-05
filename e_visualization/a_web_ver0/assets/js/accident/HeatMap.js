import { fakeApi } from "./api.js";

export default class HeatMap {
    transformData(datas) {
        // 요일별 낮/밤별 사망자/부상자 수
        // 날짜 => 요일, 낮/밤, 사망자/부상자 수
        let accidents = datas.map(e => {
            //날짜 : yyyyMMDD
            const year = e.date.substring(0, 4);
            const month = e.date.substring(4, 6);
            const date = e.date.substring(6, 8);

            const occurData = new Date(year,month-1,date);
            const week = occurData.getDate();
            
            return {
                week:week, 
                dayOrNight:e.dayOrNight, 
                deathCnt:e.deathCnt, 
                injuryCnt:e.injuryCnt
            }
        });
        const dayOrNights = Map.groupBy(accidents, ({dayOrNight}) => dayOrNight);
        const dayWeek = Map.groupBy(dayOrNights.get("day"), ({week}) => week);
        const nightWeek = Map.groupBy(dayOrNights.get("night"), ({week}) => week);
        const dayWeekSum = [];
        const nightWeekSum = [];
        dayWeek.keys().forEach(key => {
            let sum = dayWeek.get(key)
            .reduce((acc, cur) => {
                return acc += cur.deathCnt
            }, 0);

            dayWeekSum.push(sum);
        })
        nightWeek.keys().forEach(key => {
            let sum = nightWeek.get(key)
            .reduce((acc, cur) => {
                return acc += cur.deathCnt
            }, 0);

            nightWeekSum.push(sum);
        })

        return [dayWeekSum, nightWeekSum];
    }

    async drawChart(){
        document.qyerySelector("#chartBox").innerHTML = '';
        const datas = await fakeApi();
        const [dayWeekSum, nightWeekSum] = this.transformData(datas)

        var data = [
            {
                z:[dayWeekSum, nightWeekSum], 
                x:["sun","mon","tue","wed","thur","fri","sat"], 
                y:["낮", "밤"], 
                type:"heatmap", 
                hoverongaps:false, 
            }
        ];

        Plotly.newPlot("chartBox", data);
    }
}