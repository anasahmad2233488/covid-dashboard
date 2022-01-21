import Vue from 'vue'
import Home from './Home.vue'
import Predict from './Predict.vue'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false

const routes = {
  '/': Home,
  '/predict-dashboard/': Predict
}

new Vue({
  vuetify,
  //render: h => h(App)
  data: {
    currentRoute: window.location.pathname,
  },
  computed: {
    ViewComponent () { return routes[this.currentRoute] || Home }
  },
  render (h) { return h(this.ViewComponent) }
}).$mount('#app')
