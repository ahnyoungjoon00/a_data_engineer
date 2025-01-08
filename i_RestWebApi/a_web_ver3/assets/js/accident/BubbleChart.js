import { fakeApi } from "./api.js";

export default class BubbleChart {
    transformData(datas) {
        // 월정보, 사망자수, 부상자수
        const monthAccidents = datas.map(e => {
            const month = e.date.substring(4, 6) + '월';
            return {
                month: month,
                deathCnt: e.deathCnt,
                injuryCnt: e.injuryCnt,
            }
        })

        const grouped = Map.groupBy(monthAccidents, ({ month }) => month);
        const monthDeath = {}
        const monthInjury = {}
        grouped.forEach((e, key) => {
            monthDeath[key] = e.reduce((acc, cur) => acc + cur.deathCnt, 0);
            monthInjury[key] = e.reduce((acc, cur) => acc + cur.injuryCnt, 0);
        });
        return [monthDeath, monthInjury]
    }

    async drawChart() {
        document.querySelector('#chartBox').innerHTML = '';
        const datas = await fakeApi();
        const [
            monthDeath, monthInjury
        ] = this.transformData(datas);

        const deathX = Object.keys(monthDeath);
        const deathY = Object.values(monthDeath);

        var trace1 = {
            x: deathX,
            y: deathY,
            mode: 'markers',
            marker: {
                size: deathY.map(e => e / 10)
            }
        };

        const x = Object.keys(monthInjury);
        const y = Object.values(monthInjury);

        var trace2 = {
            x: Object.keys(monthInjury),
            y: Object.values(monthInjury),
            mode: 'markers',
            marker: {
                size: y.map(e => e / 10)
            }
        };

        var layout = {
            title: { text: 'Bubble Chart' },
            width: 1000,
            height: 500,
        };

        var data = [trace1, trace2];
        Plotly.newPlot('chartBox', data, layout);
    }
}