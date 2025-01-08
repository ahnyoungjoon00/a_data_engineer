import { fakeApi } from "./api.js";

export default class BoxPlots {
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

        return monthAccidents;
    }

    async drawChart() {
        document.querySelector('#chartBox').innerHTML = '';
        const datas = await fakeApi();
        const monthAccidents = this.transformData(datas);

        var trace1 = {
            y: monthAccidents.map(e => e.injuryCnt),
            x: monthAccidents.map(e => e.month),
            marker: { color: '#3D9970' },
            type: 'box'
        };

        var data = [trace1];
        Plotly.newPlot('chartBox', data);
    }
}