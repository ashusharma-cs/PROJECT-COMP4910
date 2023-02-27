
const url="http://localhost:3000/service";

const updateChart = ()=>{

  console.log('updateChart()');
  
  // fetch JSON data
  let p = fetch(url);
  
  p.then((res)=>{
    return res.json();
  }).then((res)=>{

      console.log("JSON returned " + Object.keys(res).length + " objects.");
    
      aLocation = getLocation();
      topic = getTopic();
      year = getYear();
      
      // DATE RANGE start end, on filter x > startyear x < endyear
      // implement MONTHS
      
      console.log("Location: " + aLocation);
      console.log("Topic: " + topic);
      console.log("Year: " + year);
      
      let newArray = res.filter(function (obj){
        return obj.date.slice(0,4) >= year &&
               obj.rawContent.includes(topic) == true;
      });
      // console.log(newArray);
      console.log("Amount of relevant tweets after filtering: " + newArray.length);
      
      let counter = {};
      newArray.forEach(function(obj){
        let key = obj.date.slice(0,4);
        counter[key] = (counter[key] || 0) + 1
      });

      let loccounter = {};
      newArray.forEach(function(obj){
        let key = obj.Location;
        loccounter[key] = (loccounter[key] || 0) + 1
      });
      // console.log(loccounter);
      
      // Update chart labels and data
      
      
      chart.config.data.datasets[0].label = 'Number of tweets per year';
      chart.config.data.labels = Object.keys(counter);
      chart.config.data.datasets[0].data = Object.values(counter);
      chart.update();
    })
    
  }

  const getLocation = () =>{
    // console.log(document.getElementById('location-select').value);
    return document.getElementById('location-select').value;
  }
  
  const getTopic = () =>{
    // console.log(document.getElementById('topic-input').value);
    return document.getElementById('topic-input').value;
  }
  
  const getYear = () =>{
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
      borderWidth: 1
    }]
  };

  const config = {
    type: 'line',
    data,
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  };
const chart = new Chart(ctx, config);
