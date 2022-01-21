<template>
  <v-app>
    <TopBar/>
    <v-main>
      <Dashboard ref="Dashboard"/>
    </v-main>
    <div style="height:100px"></div>
  </v-app>
</template>

<script>
import TopBar from './components/TopBar';
import Dashboard from './components/Dashboard';

//import { Config } from './config';

//const axios = require('axios').default;




export default {
  name: 'Home',
  components: {
    TopBar,
    Dashboard,
  },
  data: () => ({}),
  methods: {},
  mounted() {
  },
};
</script>
