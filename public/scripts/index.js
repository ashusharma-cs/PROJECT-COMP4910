

const url = "http://localhost:3000/service";

const updateChart = () => {

  console.log('updateChart()');

  // fetch JSON data
  let p = fetch(url);

  p.then((res) => {
    return res.json();
  }).then((res) => {

    console.log("JSON returned " + Object.keys(res).length + " objects.");

    // aLocation = getLocation();
    // topic = getTopic();

    year = getYear();


    // DATE RANGE start end, on filter x > startyear x < endyear
    // implement MONTHS

    // console.log("Location: " + aLocation);
    // console.log("Topic: " + topic);

    console.log("Year: " + year);

    let newArray = res.filter(function (obj) {
      return obj.date.slice(0, 4) == year;
    });
    // console.log(newArray);
    console.log("Amount of relevant tweets after filtering: " + newArray.length);

    const monthCounts = {};
    newArray.forEach((obj) => {
      const month = parseInt(obj.date.slice(5, 7));
      if (month in monthCounts) {
        monthCounts[month]++;
      } else {
        monthCounts[month] = 1;
      }
    });

    const sortedMonthCounts = Object.fromEntries(
      Object.entries(monthCounts).sort((a, b) => a[0] - b[0])
    );

    console.log(sortedMonthCounts);


    // console.log(monthCounts);

    // Update chart labels and data

    labels = ["January", "February", "March", "April", "May", "June", "July",
      "August", "September", "October", "November", "December"]


    chart.config.data.labels = labels;
    chart.config.data.datasets[0].data = Object.values(sortedMonthCounts);
    // chart.config.data.datasets[1].data = Object.values(sortedMonthCounts);

    let arr=Object.values(sortedMonthCounts)
    const percentArr=arr.map(num=>(num/newArray.length)*100)

    // console.log(percentarr);
    chart.config.data.datasets[1].data = percentArr;
    console.log(chart.config.data.datasets[0]);
    chart.update();
  })

}

const getLocation = () => {
  // console.log(document.getElementById('location-select').value);
  return document.getElementById('location-select').value;
}

const getTopic = () => {
  // console.log(document.getElementById('topic-input').value);
  return document.getElementById('topic-input').value;
}

const getYear = () => {
  // console.log(document.getElementById('year-select').value);
  return document.getElementById('year-select').value;
}

const canvas = document.getElementById('chart_elem');
const ctx = canvas.getContext('2d');

const data = {
  labels: [],
  datasets: [{
    label: 'Number of tweets per year',
    data: [],
    backgroundColor: [
      'rgba(255, 26, 104, 0.2)',
      'rgba(54, 162, 235, 0.2)',
      'rgba(255, 206, 86, 0.2)',
      'rgba(75, 192, 192, 0.2)',
      'rgba(153, 102, 255, 0.2)',
      'rgba(255, 159, 64, 0.2)',
      'rgba(0, 0, 0, 0.2)'
    ],
    borderColor: [
      'rgba(255, 26, 104, 1)',
      'rgba(54, 162, 235, 1)',
      'rgba(255, 206, 86, 1)',
      'rgba(75, 192, 192, 1)',
      'rgba(153, 102, 255, 1)',
      'rgba(255, 159, 64, 1)',
      'rgba(0, 0, 0, 1)'
    ],
    borderWidth: 1,
    yAxisID: 'y'
  }, {
    label: 'Percentage of tweets per year',
    data: [],
    backgroundColor: [
      'rgba(255, 26, 104, 0.2)',
      'rgba(54, 162, 235, 0.2)',
      'rgba(255, 206, 86, 0.2)',
      'rgba(75, 192, 192, 0.2)',
      'rgba(153, 102, 255, 0.2)',
      'rgba(255, 159, 64, 0.2)',
      'rgba(0, 0, 0, 0.2)'
    ],
    borderColor: [
      'rgba(255, 26, 104, 1)',
      'rgba(54, 162, 235, 1)',
      'rgba(255, 206, 86, 1)',
      'rgba(75, 192, 192, 1)',
      'rgba(153, 102, 255, 1)',
      'rgba(255, 159, 64, 1)',
      'rgba(0, 0, 0, 1)'
    ],
    tension: 0.4,
    type: 'line',
    yAxisID: 'percentage'
  }]
};

const config = {
  type: 'bar',
  data,
  options: {
    scales: {
      y: {
        beginAtZero: true,
        type: 'linear',
        position: 'left',
        grace: '2%'
      },
      percentage: {
        beginAtZero: true,
        type: 'linear',
        position: 'right',
        min:0,
        max: 30,
        grace: '2%',
        // ticks: {
        //   stepSize: 5
        // }
      }
    }
  }
};
const chart = new Chart(ctx, config);
