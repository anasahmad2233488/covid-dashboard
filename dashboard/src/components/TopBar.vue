<template>
  <v-app-bar
  app
  dark
  >
  <ul>
    <li><v-btn
      color="primary"
      href="/"
      rel="noopener">Dashboard</v-btn></li>
    <li><v-btn
      color="primary"
       href="/predict-dashboard/"
       rel="noopener">Predict</v-btn></li>
  </ul>
  <v-spacer></v-spacer>
  <v-toolbar-title class="flex text-center white--text">
    COVID-19 MALAYSIA: ANALYTICS DASHBOARD
  </v-toolbar-title>
  <v-spacer></v-spacer>
  <v-spacer></v-spacer>
  <v-spacer></v-spacer>
  </v-app-bar>
</template>

<script>
export default {
  name: 'TopBar',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
.v-application a {
  color: black;
}
.v-btn{
  color: black !important;
}
.v-btn:hover {
  background-color: DodgerBlue;
}
.v-sheet {
  background-color: DodgerBlue !important;
}

</style>
