  var margin = 100,
      w = 8,
      h = 500,
      data = [],
      chart = [],
      bars,
      x, y, xAxis, yAxis;

  var results = d3.map( playlist_json );

  results.forEach( function( key, val) {
    var result = {};
    result.bucket = val.month;
    result.songs = val.value;
    data.push(result)
  });

  chart = d3.select("#bar-results").append("svg")
    .attr("class", "chart")
    .attr("width", 1100)
    .attr("height", h)
    .append("g");

  d3.select("svg g")
    .attr("transform", "translate(50, 50)");

  x = d3.scale.ordinal()
    .domain(data.map(function(d) {return d.bucket }));

  y = d3.scale.linear()
    .range([height, 0]);

  bars = chart.append("g")
    .attr("class", "bars");

  bars.selectAll("rect")
    .data( data )
    .enter().append("rect")
    .attr("x", function(d, i) { return x( d.bucket ) - .5;})
    .attr("y", function(d) { return (h - margin) - y( d.songs ) + .5})
    .attr("width", w)
    .append("g")


  xAxis = d3.svg.axis()
      .scale(x)
      .ticks(20)
      .tickSize(6, 3, 1)

      .orient("bottom");

  yAxis = d3.svg.axis()
      .scale(d3.scale.linear().domain( [0, d3.max( data, function( d) { return d.songs;})]).rangeRound( [h = margin, 0]))
      .tickSize(6, 3, 1)
      .orient("left")

  chart.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + (h - margin) + ")")
    .call(xAxis)

  chart.append("g")
    .attr("class", "y axis")
    .attr("transform", "translate(0," + x.range()[1] + ")")
    .call(yAxis);

