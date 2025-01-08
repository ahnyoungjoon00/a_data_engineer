import { fakeApi } from "./api.js";

export default class Histogram {
    // 일별 사망, 부상사고 건수를 scatter chart로 작성
    transformData(datas) {
        // 월정보, 사망자수, 부상자수
        const dateAccidents = datas.map(e => {
            const date = e.date.substring(4, 6) + '/' + e.date.substring(6, 8);
            return {
                date: date,
                deathCnt: e.deathCnt,
                injuryCnt: e.injuryCnt,
            }
        })

        const grouped = Map.groupBy(dateAccidents, ({ date }) => date);
        const dateDeath = {}
        const dateInjury = {}

        grouped.forEach((e, key) => {
            dateDeath[key] = e.reduce((acc, cur) => acc + cur.deathCnt, 0);
            dateInjury[key] = e.reduce((acc, cur) => acc + cur.injuryCnt, 0);
        });

        return [dateDeath, dateInjury]
    }

    async drawChart() {
        document.querySelector('#chartBox').innerHTML = '';
        const datas = await fakeApi();
        const [
            dateDeath, dateInjury
        ] = this.transformData(datas);

        var death = {
            x: Object.values(dateDeath),
            type: "histogram",
            opacity: 0.5,
            marker: {
                color: 'green',
            },
            name: 'death',
        };

        var injury = {
            x: Object.values(dateInjury),
            type: "histogram",
            opacity: 0.6,
            marker: {
                color: 'red',
            },
            name: 'injury',
        };

        var data = [death, injury];
        var layout = { barmode: "overlay" };
        Plotly.newPlot('chartBox', data, layout);
    }
}