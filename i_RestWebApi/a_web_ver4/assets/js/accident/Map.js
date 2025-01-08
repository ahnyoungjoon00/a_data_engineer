import { fakeApi } from "./api.js";

export default class MapChart {
    transformData(datas) {
        const accidents = datas.map(e => {
            let info = `${e.date.substring(4, 6)}/${e.date.substring(6, 8)}
                사망:${e.deathCnt}
                부상:${e.injuryCnt}
            `;
            return {
                info: info,
                lat: e.lat,
                lng: e.lng,
            }
        })

        return accidents;
    }

    async drawChart() {
        document.querySelector('#chartBox').innerHTML = '';
        const datas = await fakeApi();
        const accidents = this.transformData(datas);

        var data = [
            {
                type: "scattermap",
                text: accidents.map(e => e.info),
                lon: accidents.map(e => e.lng),
                lat: accidents.map(e => e.lat),
                marker: { color: "fuchsia", size: 4 }
            }
        ];

        var layout = {
            dragmode: "zoom",
            map: { style: "open-street-map", center: { lat: 37, lon: 127 }, zoom: 3 },
            margin: { r: 0, t: 0, b: 0, l: 0 }
        };

        Plotly.newPlot("chartBox", data, layout);
    }
}