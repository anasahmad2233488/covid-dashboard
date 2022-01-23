<template>
  <v-app>
    <TopBar/>
    <v-main>
      <v-container max-width="700px">
      <v-row>
        <div style="width:100%" class="text-center mt-10 mb-10 ml-3 mr-3">This tool is for predicting the number of COVID-19 daily new cases. You may select for which state you wish to predict for. Explore the possiblity of having different number of people mobility, abient temperature, and total vaccinated population.</div>
      </v-row>
      <v-row>
        <v-divider></v-divider>
      </v-row>
        <v-row class="text-center">
          <v-col cols="12">
            <MultiLineChart
              ref="line_chart"
              v-bind:chart_data="chart_data"
            />
          </v-col>
        </v-row>
        <v-row>
          <v-divider></v-divider>
        </v-row>
        <v-row>
          <v-col cols="3">
          </v-col>
          <v-col cols="4">
            <v-select
              v-model="data_select"
              :items="data_items"
              item-text="name"
              item-value="name"
              label="Predict"
              persistent-hint
              return-object
            ></v-select>
          </v-col>
          <v-col cols=2>
            <v-btn
              color='mediumturquoise'
              @click='update()'
            >PREDICT</v-btn>
         </v-col>
        </v-row>
		<v-row class="text-center">
     <v-col cols="3">
     </v-col>
      <v-col cols="3">
         <v-dialog
           ref="date_dialog"
           v-model="date_modal"
           :return-value.sync="date"
           persistent
           width="290px"
         >
           <template v-slot:activator="{ on, attrs }">
             <v-text-field
               v-model="date"
               label="Date"
               prepend-icon="mdi-calendar"
               readonly
               v-bind="attrs"
               v-on="on"
             ></v-text-field>
           </template>
           <v-date-picker
             v-model="date"
             scrollable
           >
             <v-spacer></v-spacer>
             <v-btn
               text
               color="primary"
               @click="date_modal = false"
             >
               Cancel
             </v-btn>
             <v-btn
               text
               color="primary"
               @click="$refs.date_dialog.save(date)"
             >
               OK
             </v-btn>
            </v-date-picker>
            </v-dialog>
            </v-col>
           <v-col cols="3">
             <v-select
               v-model="state_select"
               :hint="`${state_select.abbr}`"
               :items="state_items"
               item-text="state"
               item-value="val"
               label="State"
               persistent-hint
               return-object
             ></v-select>
           </v-col>

         </v-row>
          <v-row>
           <v-col cols="3">
           </v-col>
           <v-col cols="3">
             <label  for="temp">Average Temperature: {{temp}}&#8451;</label>
             <input style="width:100%" name="temp" v-model.number="temp" type="range" min="20" max="32" step="0.01">
           </v-col>
           <v-col cols="3">
             <label  for="percent_vax">Percentage Vaccinated: {{percent_vax}}%</label>
             <input style="width:100%" name="percent_vax" v-model.number="percent_vax" type="range" min="0" max="100">
           </v-col>
        </v-row>
         <v-row>
          <v-col cols="3">
          </v-col>
          <v-col cols="3">
            <label  for="checkins">Average MySJ Checkins (percentage population): {{checkins}}%</label>
            <input style="width:100%" name="checkins" v-model.number="checkins" type="range" min="0" max="150" step="0.01">
          </v-col>
       </v-row>
      </v-container>
    </v-main>
    <div style="height:100px"></div>
  </v-app>
</template>

<script>
import TopBar from './components/TopBar';
import MultiLineChart from './components/MultiLineChart';

const axios = require('axios').default;

export default {
  name: 'Predict',
  components: {
    TopBar,
    MultiLineChart
  },
  data: () => ({
          chart_data:[{"date":"2013-04-28","value":0},{"date":"2013-04-29","value":0}],
          api_base_url: null,
          api_url: {
            'cases_new': 'predict/cases/',
            'cases_death': 'predict/death/'
          },
          state_select: {state:'Johor', abbr: 'JHR', val: 2},
          state_items: [
            //{state:'Malaysia', abbr: 'MYS', val: 1},
            {state:'Johor', abbr: 'JHR', val: 2},
            {state:'Kedah', abbr: 'KDH', val: 3},
            {state:'Kelantan', abbr: 'KTN', val: 4},
            {state:'Melaka', abbr: 'MLK', val: 5},
            {state:'Negeri Sembilan', abbr: 'NSN', val: 6},
            {state:'Pahang', abbr: 'PHG', val: 7},
            {state:'Pulau Pinang', abbr: 'PNG', val: 8},
            {state:'Perak', abbr: 'PRK', val: 9},
            {state:'Perlis', abbr: 'PLS', val: 10},
            {state:'Selangor', abbr: 'SGR', val: 11},
            {state:'Terengganu', abbr: 'TGN', val: 12},
            {state:'Sabah', abbr: 'SBH', val: 13},
            {state:'Sarawak', abbr: 'SWK', val: 14},
            {state:'W.P. Kuala Lumpur', abbr: 'WKL', val: 15},
            {state:'W.P. Labuan', abbr: 'WLB', val: 16},
            {state:'W.P. Putrajaya', abbr: 'WPJ', val: 17},
          ],
          data_select: { name: 'New Cases', value: 'cases_new'},
          data_items: [
            { name: 'New Cases', value: 'cases_new'},
            { name: 'Death', value: 'cases_death'},
          ],
          date: (new Date('2021-01-01')).toISOString().substr(0, 10),
          date_menu: false,
          date_modal: false,
          date_menu2: false,
          temp:26.5,
          percent_vax: 100,
          checkins: 60,
		}),
  mounted() {
		this.api_base_url = process.env.VUE_APP_ROOT_API;
		this.update();
  },
  methods: {
	update: function(){
          var state = this.state_select.val;
          var date = this.date;
          var checkins = this.checkins;
          var temp = this.temp;
          var percent_vax = this.percent_vax;

          var target = this.data_select.value;
          var api_url = this.api_url[target];

          axios.get(this.api_base_url+api_url+'?state='+state+'&date='+date+'&checkins='+checkins+'&percent_vax='+percent_vax+'&temp='+temp)
                .then( response => {
                  var chart_data = []
                  response.data.forEach(function(d) {
                    chart_data.push({"date": d.date, "name": d.name, "value": d[target]})
                  });
                  this.$refs.line_chart.var_name= this.data_select.name;
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

  .white{
    color:white !important;
      background-color: rgb(18,18,18) !important;
  }

  input{
    font-size:14px;
    color:#FFFFFFB3;
  }

  label{
    font-size:12px;
    color:#FFFFFFB3;
  }


  </style>
