
const url="http://localhost:3000/service";




const updateChart = ()=>{

    let p= fetch(url);

p.then((res)=>{
    return res.json();
}).then((res)=>{

    const full_date=res.map((item)=>{
        return item.date.slice(0,10)
    });

    numtweets_2018 = numtweets_2019 = numtweets_2020 = numtweets_2021 = numtweets_2022 = numtweets_2023 = numtweets_other = 0;

    for(let i = 0; i < full_date.length; i++){
        switch(full_date[i].slice(0,4)){
          case '2018':
            numtweets_2018++;
            continue;
          case '2019':
            numtweets_2019++;
            continue;
          case '2020':
            numtweets_2020++;
            continue;
          case '2021':
            numtweets_2021++;
            continue;
          case '2022':
            numtweets_2022++;
            continue;
          case '2023':
            numtweets_2023++;
            continue;
          default:
            numtweets_other++;
            continue;
        };
      };

      years = ['2018','2019','2020','2021','2022','2023','Other'];
      tweetsperyear = [numtweets_2018, numtweets_2019, numtweets_2020, numtweets_2021, numtweets_2022, numtweets_2023,numtweets_other];

      // Update chart labels and data
      
      // myChart.config.data.datasets[0].label = '';
      chart.config.data.labels = years;
      chart.config.data.datasets[0].data = tweetsperyear;
      chart.update();
})

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
