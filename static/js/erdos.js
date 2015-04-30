//WORK - Resize box height based on width
var cw = $('.article-box').width();
$('.article-box').css({'height':cw+'px'});

//D3 Stuff
var createGraph = function(data){
  console.log(data);
  /* d3 setup */
  var width = 590;
  var height = 400;

  var svg = d3.select("#chartContainer")
    .append("svg")
      .attr("width", width)
      .attr("height", height)
    .append('g')
        .attr('class','chart');

  /*
    Dimple.js Chart construction code
  */

  var myChart = new dimple.chart(svg, data);
  var x = myChart.addCategoryAxis("x", ["Yes", "No", "Awaiting"]); 
  myChart.addMeasureAxis("y", "Reviews");
  myChart.addSeries(null, dimple.plot.bar);
  myChart.draw();
};

    //myChart.setBounds(60, 30, 510, 305)