<template>
  <v-col id="my_dataviz" />
</template>

<script>
import * as d3 from "d3";

export default {
  name: "Chart",
  props: {
    chart_data: Array,
  },
  data() {
    return {
      dat: ['asd'],
      svg: null,
      height: null,
      width: null,
      g_x: null,
      g_y: null
    };
  },
  mounted() {
    var margin = {top: 20, right: 20, bottom: 50, left: 70},
        width = 750 - margin.left - margin.right,
        height = 400 - margin.top - margin.bottom;

    this.height = height;
    this.width = width;


    // append the svg obgect to the body of the page
    // appends a 'group' element to 'svg'
    // moves the 'group' element to the top left margin
    this.svg = d3.select("#my_dataviz").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
      .append("g")
        .attr("transform",
              "translate(" + margin.left + "," + margin.top + ")");

    this.primary_chart = this.svg.append("path");
    this.g_x = this.svg.append("g")
        .attr("transform", "translate(0," + this.height + ")");
    this.g_y = this.svg.append("g");

    this.generateArc(this.chart_data);
  },
  updated(){
  },
  methods: {
    generateArc(json_data) {
      // parse the date / time
      var parseTime = d3.timeParse("%Y-%m-%d");
      var bisectDate = d3.bisector(function(d) { return d.date; }).left;
      var dateFormatter = d3.timeFormat("%d/%m/%Y");

      // set the ranges
      var x = d3.scaleTime().range([0, this.width]);
      var y = d3.scaleLinear().range([this.height, 0]);

      // define the line
      var valueline = d3.line()
          .x(function(d) { return x(d.date); })
          .y(function(d) { return y(d.value); });

        // format the data
        json_data.forEach(function(d) {
            d.date_text = d.date;
            d.date = parseTime(d.date);
        });

        json_data.sort(function(a, b) {
            return a.date - b.date;
        });

        // Add the x Axis
        x.domain(d3.extent(json_data, function(d) { return d.date; }));
        y.domain([0, d3.max(json_data, function(d) { return parseFloat(d.value); })]);

        this.primary_chart
                .data([json_data])
                .attr("class", "line")
                .attr("d", valueline);

        this.g_x.transition().duration(1000)
            .attr("transform", "translate(0," + this.height + ")")
            .call(d3.axisBottom(x).tickFormat(function(d) { return dateFormatter(d); }));

        this.g_x.selectAll('text')
            .attr("dx", "1em")
            .attr("dy", "2em")
            .attr("transform", "rotate(35)");

        // Add the y Axis
        this.g_y.transition().duration(1000)
            .call(d3.axisLeft(y));

        var focus = this.svg.append("g")
                    .attr("class", "focus")
                    .style("display", "none");

        var focus_circle = focus.append("circle")
                    .attr("r", 5);

                focus.append("rect")
                    .attr("class", "tooltip")
                    .attr("width", 100)
                    .attr("height", 50)
                    .attr("x", 10)
                    .attr("y", -22)
                    .attr("rx", 4)
                    .attr("ry", 4);

                focus.append("text")
                    .attr("class", "tooltip-date")
                    .attr("x", 18)
                    .attr("y", -2);

                focus.append("text")
                    .attr("x", 18)
                    .attr("y", 18)
                    .text("Value:");

                focus.append("text")
                    .attr("class", "tooltip-value")
                    .attr("x", 60)
                    .attr("y", 18);

                this.svg.append("rect")
                    .attr("class", "overlay")
                    .attr("width", this.width)
                    .attr("height", this.height)
                    .on("mouseover", function() { focus.style("display", null); })
                    .on("mouseout", function() { focus.style("display", "none"); })
                    .on("mousemove", mousemove);

                function mousemove() {
                    var x0 = x.invert(d3.pointer(event)[0]);
                    var i = bisectDate(json_data, x0, 1);
					
					if (i<json_data.length){
						var d0 = json_data[i - 1],
							d1 = json_data[i],
							d = x0 - d0.date > d1.date - x0 ? d1 : d0;

						var x_trans = x(d.date);
						var y_trans = y(d.value)
						if (x_trans > 550){
							x_trans -= 120;
							focus_circle.attr("transform", "translate(120,0)");
						} else {
						focus_circle.attr("transform", "translate(0,0)");
						}
						focus.attr("transform", "translate(" + x_trans + "," + y_trans + ")");
						focus.select(".tooltip-date").text(dateFormatter(d.date));
						focus.select(".tooltip-value").text(d.value);					
					}
                }

    },
    updateChart(chart_data) {
      // Add X axis --> it is a date format
      this.generateArc(chart_data);

    }
  }
};

</script>

<style>
.line {
  fill: none;
  stroke: #4169E1;
  stroke-width: 2px;
}

.overlay {
        fill: none;
        pointer-events: all;
    }

    .focus circle {
        fill: steelblue;
    }

    .focus text {
        font-size: 14px;
    }

    .tooltip {
        fill: white;
        stroke: #000;
    }

    .tooltip-date, .tooltip-likes {
        font-weight: bold;
    }
</style>
