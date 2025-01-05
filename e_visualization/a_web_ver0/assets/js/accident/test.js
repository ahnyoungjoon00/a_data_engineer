const exmp = "2023010107";
const dateObj = exmp.substring(0, 8)
const year = dateObj.substring(0,4);
const month = dateObj.substring(4,6);
const day = dateObj.substring(6,8);
const date = new Date(year, month, day);
const dayOfweek = date.getDay();
console.log(date);
console.log(typeof(dayOfweek), dayOfweek);

var data = [
    {
      x: dayOfweek,
      y: dayOrNight,
      z: [[1, null, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
      type: 'heatmap',
      hoverongaps: false
    }
  ];
  
  Plotly.newPlot('myDiv', data);