<template>
  <v-container max-width="700px">
    <v-row>
      <v-col></v-col>
      <v-col cols="8">
        <div style="" class="text-center mt-10 mb-10 ml-3 mr-3">Explore Malaysia COVID-19 data. Select the period between which you wish the statistics to be presented to you.</div>
      </v-col>
      <v-col></v-col>
    </v-row>
    <v-row class="text-center">
      <v-col cols="2">
        <v-select
          v-model="data_select"
          :items="data_items"
          item-text="name"
          item-value="name"
          label="Chart Data"
          persistent-hint
          return-object
        ></v-select>
      </v-col>
      <v-col cols="2">
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
      <v-col>
        <v-dialog
          ref="start_date_dialog"
          v-model="start_date_modal"
          :return-value.sync="start_date"
          persistent
          width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="start_date"
              label="Start Date"
              prepend-icon="mdi-calendar"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
            v-model="start_date"
            scrollable
          >
            <v-spacer></v-spacer>
            <v-btn
              text
              color="primary"
              @click="start_date_modal = false"
            >
              Cancel
            </v-btn>
            <v-btn
              text
              color="primary"
              @click="$refs.start_date_dialog.save(start_date)"
            >
              OK
            </v-btn>
          </v-date-picker>
        </v-dialog>
      </v-col>
      <v-col>
         <v-dialog
           ref="end_date_dialog"
           v-model="end_date_modal"
           :return-value.sync="end_date"
           persistent
           width="290px"
         >
           <template v-slot:activator="{ on, attrs }">
             <v-text-field
               v-model="end_date"
               label="End Date"
               prepend-icon="mdi-calendar"
               readonly
               v-bind="attrs"
               v-on="on"
             ></v-text-field>
           </template>
           <v-date-picker
             v-model="end_date"
             scrollable
           >
             <v-spacer></v-spacer>
             <v-btn
               text
               color="primary"
               @click="end_date_modal = false"
             >
               Cancel
             </v-btn>
             <v-btn
               text
               color="primary"
               @click="$refs.end_date_dialog.save(end_date)"
             >
               OK
             </v-btn>
           </v-date-picker>
         </v-dialog>
      </v-col>
      <v-col cols=2>
        <v-btn
          color='mediumturquoise'
          @click='update()'
        >UPDATE</v-btn>
     </v-col>
    </v-row>
    <v-row class="text-center">
      <v-col cols="12">
        <LineChart
          ref="line_chart"
          v-bind:chart_data="chart_data"
          v-bind:x_axis="data_select.name"
        />
      </v-col>
    </v-row>
    <v-row>
      <v-divider></v-divider>
    </v-row>
    <v-row class="text-center">
      <v-col cols=12>
        <center class="pt-6 pb-6">
          Statistics for the day <b>{{updated_end_date}}</b>.
        </center>
      </v-col>
    </v-row>
    <v-row class="text-center">
      <v-col style="font-size:14px">
        <u>Cases</u>
      </v-col>
    </v-row>
    <v-row class="text-center">
      <v-col
       cols="3"
       class="d-flex flex-column"
       v-for="item in items.daily_cases"
       :key="item.id"
       >
        <v-card class="card flex d-flex flex-column"
          elevation="2"
          style="flex: auto"
        >
        <v-card-title class="p"
        >
          {{ item.name }}
        </v-card-title>
        <v-card-text
          class="card-text mb-4"
        >
          {{ item.value }}
        </v-card-text>
      </v-card>
      </v-col>
    </v-row>
    <v-row class="text-center">
      <v-col style="font-size:14px">
        <u>Testing</u>
      </v-col>
    </v-row>
    <v-row class="text-center">
      <v-col
       cols="3"
       class="d-flex flex-column"
       v-for="item in items.daily_testing"
       :key="item.id"
       >
        <v-card class="card flex d-flex flex-column"
          elevation="2"
          style="flex: auto"
        >
        <v-card-title class="p"
        >
          {{ item.name }}
        </v-card-title>
        <v-card-text
          class="card-text mb-4"
        >
          {{ item.value }}
        </v-card-text>
      </v-card>
      </v-col>
    </v-row>
    <v-row class="text-center">
      <v-col style="font-size:14px">
        <u>MySejahtera Checkins</u>
      </v-col>
    </v-row>
    <v-row class="text-center">
      <v-col
       cols="3"
       class="d-flex flex-column"
       v-for="item in items.daily_mysj"
       :key="item.id"
       >
        <v-card class="card flex d-flex flex-column"
          elevation="2"
          style="flex: auto"
        >
        <v-card-title class="p"
        >
          {{ item.name }}
        </v-card-title>
        <v-card-text
          class="card-text mb-4"
        >
          {{ item.value }}
        </v-card-text>
      </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-divider></v-divider>
    </v-row>
    <v-row class="text-center">
      <v-col cols=12>
        <center class="pt-6 pb-6">
          Statistics for the period between <b>{{updated_start_date}}</b> and <b>{{updated_end_date}}</b>.
        </center>
      </v-col>
    </v-row>
    <v-row class="text-center">
      <v-col
       cols="3"
       class="d-flex flex-column"
       v-for="item in items.aggregated"
       :key="item.id"
       >
        <v-card class="card flex d-flex flex-column"
          elevation="2"
          style="flex: auto"
        >
        <v-card-title class="p"
        >
          {{ item.name }}
        </v-card-title>
        <v-card-text
          class="card-text mb-4"
          style="font-size:20px;"
        >
          {{ item.value }}
        </v-card-text>
      </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import LineChart from './LineChart';

const axios = require('axios').default;
const anime = require('animejs').default;

export default {
  name: 'Dashboard',

  components: {
    LineChart
  },

  data () {
    return {
      chart_data:[
        {"date":"2013-04-28","value":0},{"date":"2013-04-29","value":0}],
        items: {
          daily_cases:[
            { id: 1, name: 'New Cases', value: '0'},
            { id: 2, name: 'Recoveries', value: '0'},
            { id: 3, name: 'Deaths', value: '0'},
            { id: 4, name: 'Active Cases', value: '0'},
            { id: 5, name: 'New Cases (per 1M pop)', value: '0'},
            { id: 6, name: 'Recoveries (per 1M pop)', value: '0'},
            { id: 7, name: 'Deaths (per 1M pop)', value: '0'},
            { id: 8, name: 'Active Cases (per 1M pop)', value: '0'},
          ],
          daily_testing:[
            { id: 9, name: 'Test: rtk_ag', value: '0'},
            { id: 10, name: 'Test: pcr', value: '0'},
            { id: 11, name: 'Test: total', value: '0'},
            { id: 12, name: 'Test: rtk_ag (per 1M pop)', value: '0'},
            { id: 13, name: 'Test: pcr (per 1M pop)', value: '0'},
            { id: 14, name: 'Test: total (per 1M pop)', value: '0'},
          ],
          daily_mysj:[
            { id: 15, name: 'MySJ Checkins', value: '0'},
            { id: 16, name: 'MySJ Total Individuals', value: '0'},
            { id: 17, name: 'MySJ Total Places', value: '0'},
            { id: 18, name: 'MySJ Ind to Checkin ratio', value: '0'},
            { id: 19, name: 'MySJ Ind: Pop Percentage', value: '0'},
          ],
          aggregated:[
            { id: 1, name: 'Total Days', value: '0'}, //total_days
            { id: 2, name: 'Total New Cases', value: '0'}, //total_new_cases
            { id: 3, name: 'Total Deaths', value: '0'}, //total_deaths
            { id: 4, name: 'Total Recovery', value: '0'}, //total_recovery
            { id: 5, name: 'Total Active Clusters', value: '0'}, //count_active_clusters
            { id: 6, name: 'Total Rtk-Ag Tests', value: '0'}, //total_rtk_ag
            { id: 7, name: 'Total PCR Tests', value: '0'}, //total_pcr
            { id: 8, name: 'Total Checkins', value: '0'}, //total_checkins
          ],
        },
        chart_data_list: {
          1: {url: 'cases/daily-new-cases/', var: 'cases_new'},
          2: {url: 'cases/death/', var: 'cases_death'},
          3: {url: 'cases/recovery/', var: 'cases_recovered'},
          4: {url: 'cases/total-cases/', var: 'cases_active'},
          5: {url: 'vaccine/completed-vaccination/', var: 'cumul_full'},
          6: {url: 'facility/hospital-admission/', var: 'admitted_covid'},
          7: {url: 'facility/icu-admission/', var: 'icu_covid'},
          8: {url: 'facility/pkrc-admission/', var: 'admitted_covid'},
          9: {url: 'cases/checkins/', var: 'checkins'},
          10: {url: 'cases/individual-checkins/', var: 'unique_ind'},
          11: {url: 'cases/checkin-locations/', var: 'unique_loc'},
        },
        state_select: {state:'Malaysia', abbr: 'MYS', val: 1},
        state_items: [
          {state:'Malaysia', abbr: 'MYS', val: 1},
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
        data_select: { name: 'New Cases', value: '1'},
        data_items: [
          { name: 'New Cases', value: '1'},
          { name: 'Death', value: '2'},
          { name: 'Recovery', value: '3'},
          { name: 'Active Cases', value: '4'},
          { name: 'Total Full Vaccination', value: '5'},
          { name: 'Hospitals Admission', value: '6'},
          { name: 'ICU Admission', value: '7'},
          { name: 'PKRC Admission', value: '8'},
          { name: 'Checkins', value: '9'},
          { name: 'Checkin Individuals', value: '10'},
          { name: 'Checkin Locations', value: '11'},
        ],
        start_date: (new Date('2021-01-01')).toISOString().substr(0, 10),
        end_date: (new Date('2021-12-01')).toISOString().substr(0, 10),

        updated_start_date: null,
        updated_end_date: null,

        start_date_menu: false,
        start_date_modal: false,
        start_date_menu2: false,
        end_date_menu: false,
        end_date_modal: false,
        end_date_menu2: false,

		api_url: null,
      }
    },
    mounted() {
		this.api_url = process.env.VUE_APP_ROOT_API;
    this.$refs.line_chart.x_axis = "asdsads";
		this.update();
    },
    methods: {

      update: function(){
        var chart_data_url = this.chart_data_list[this.data_select.value].url;
        var state = this.state_select.val;

        this.updated_start_date = this.start_date;
        this.updated_end_date = this.end_date;

        // update chart
       axios.get(this.api_url+chart_data_url+'?state='+state+'&date__gte='+this.start_date+'&date__lte='+this.end_date)
        .then( response => {

          var var_name = this.chart_data_list[this.data_select.value].var;
          var chart_data = []
          response.data.forEach(function(d) {
            chart_data.push({"date": d.date, "value": d[var_name]})
          });
          this.$refs.line_chart.updateChart(chart_data);

        });

        axios.get(this.api_url+'cases/cases-summary/?state='+state+'&date='+this.end_date)
        .then( response => {
          // update data cards cases
          if(response.data.length>0){
            this.setDailyCount(0, response.data[0]['cases_new']);
            this.setDailyCount(1, response.data[0]['cases_recovered']);
            this.setDailyCount(2, response.data[0]['cases_death']);
            this.setDailyCount(3, response.data[0]['cases_active']);
            this.setDailyCount(4, response.data[0]['cases_new_per_population']*1000000);
            this.setDailyCount(5, response.data[0]['cases_recovered_per_population']*1000000);
            this.setDailyCount(6, response.data[0]['cases_death_per_population']*1000000);
            this.setDailyCount(7, response.data[0]['cases_active_per_population']*1000000);
          }
        });

        axios.get(this.api_url+'cases/tests-summary/?state='+state+'&date='+this.end_date)
        .then( response => {
          // update data cards tests
          if(response.data.length>0){
            this.setDailyCount(8, response.data[0]['rtk_ag']);
            this.setDailyCount(9, response.data[0]['pcr']);
            this.setDailyCount(10, response.data[0]['total_tests']);
            this.setDailyCount(11, response.data[0]['rtk_ag_per_population']*1000000);
            this.setDailyCount(12, response.data[0]['pcr_per_population']*1000000);
            this.setDailyCount(13, response.data[0]['total_tests_per_population']*1000000);
          }
        });

        axios.get(this.api_url+'cases/checkin-summary/?state='+state+'&date='+this.end_date)
        .then( response => {
          // update data cards tests
          if(response.data.length>0){
            this.setDailyCount(14, response.data[0]['checkins']);
            this.setDailyCount(15, response.data[0]['unique_ind']);
            this.setDailyCount(16, response.data[0]['unique_loc']);
            this.setDailyCount(17, response.data[0]['checkins_to_ind_ratio']);
            this.setDailyCount(18, (response.data[0]['unique_ind_per_population']*100)+"%");
          }
        });

        axios.get(this.api_url+'cases/cases-summary-period/?state='+state+'&start_date='+this.start_date+'&end_date='+this.end_date)
        .then( response => {
          // update data cards tests
          if(response.data){
            this.setAggregateCount(0, response.data['total_days']);
            this.setAggregateCount(1, response.data['total_new_cases']);
            this.setAggregateCount(2, response.data['total_deaths']);
            this.setAggregateCount(3, response.data['total_recovery']);
          }
        });

        axios.get(this.api_url+'cases/cluster-summary-period/?state='+state+'&start_date='+this.start_date+'&end_date='+this.end_date)
        .then( response => {
          // update data cards tests
          if(response.data){
            this.setAggregateCount(4, response.data['count_active_clusters']);
          }
        });

        axios.get(this.api_url+'cases/tests-summary-period/?state='+state+'&start_date='+this.start_date+'&end_date='+this.end_date)
        .then( response => {
          // update data cards tests
          if(response.data){
            this.setAggregateCount(5, response.data['total_rtk_ag']);
            this.setAggregateCount(6, response.data['total_pcr']);
          }
        });

        axios.get(this.api_url+'cases/checkin-summary-period/?state='+state+'&start_date='+this.start_date+'&end_date='+this.end_date)
        .then( response => {
          // update data cards tests
          if(response.data){
            this.setAggregateCount(7, response.data['total_checkins']);
          }
        });

      },
      setDailyCount (index, val) {
        const obj = { n: this.items.daily[index].value }
        anime({
          targets: obj,
          n: val,
          round: 1,
          duration: 500,
          easing: 'linear',
          update: () => {
            this.items.daily[index].value = obj.n.toLocaleString()
          }
        })
      },
      setAggregateCount (index, val) {
        const obj = { n: this.items.aggregated[index].value }
        anime({
          targets: obj,
          n: val,
          round: 1,
          duration: 500,
          easing: 'linear',
          update: () => {
            this.items.aggregated[index].value = obj.n.toLocaleString()
          }
        })
      }
    }

  }
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
