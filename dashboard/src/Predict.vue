<template>
  <v-app>
    <TopBar/>
    <v-main>
      <v-container max-width="700px">
        <v-row class="text-center">
          <v-col cols="12">
            <LineChart
              ref="line_chart"
              v-bind:chart_data="chart_data"
            />
          </v-col>
        </v-row>
        <v-row>
          <v-divider></v-divider>
        </v-row>
		<v-row class="text-center">
          <v-col cols=2>
            <v-btn
              color='mediumturquoise'
              @click='update()'
            >UPDATE</v-btn>
         </v-col>
        </v-row>
      </v-container>
    </v-main>
    <div style="height:100px"></div>
  </v-app>
</template>

<script>
import TopBar from './components/TopBar';
import LineChart from './components/LineChart';

const axios = require('axios').default;

export default {
  name: 'Predict',
  components: {
    TopBar,
    LineChart
  },
  data: () => ({		
        chart_data:[{"date":"2013-04-28","value":0},{"date":"2013-04-29","value":0}],
		api_url: null,
		}),
  mounted() {
		this.api_url = process.env.VUE_APP_ROOT_API;
		this.update();
  },
  methods: {
	update: function(){
	var state = 1;
	var start_date = '2021-01-01';
	var end_date = '2021-12-01';
	
	axios.get(this.api_url+'cases/daily-new-cases/'+'?state='+state+'&date__gte='+start_date+'&date__lte='+end_date)
        .then( response => {
          var var_name = 'cases_new';
          var chart_data = []
          response.data.forEach(function(d) {
            chart_data.push({"date": d.date, "value": d[var_name]})
          });
          this.$refs.line_chart.updateChart(chart_data);
        });
	}
  },
};
</script>

  <style scoped>
  .container{
    max-width:830px;
    min-width:630px;
  }
  .card{
    min-width:150px;
    max-width:200px;
  }

  .v-card__title{
    font-size:12px;
    padding: 6px 12px 0 12px;
    color: steelblue;
  }

  b {
    color: steelblue;
  }

  .card-text {
    font-size:24px;
    font-weight: 700;
    padding: 16px 16px 16px 16px;
  }

  .mediumturquoise {
    background-color: MediumTurquoise !important;
    color: Black !important;
  }

  .v-input{
    font-size:12px;
  }
  </style>
