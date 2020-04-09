// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)
Vue.prototype.$axios = axios;
// Vue.prototype.$router = router;
Vue.config.productionTip = false

// Vue.prototype.$http = axios.create({
//   // baseURL: "http://127.0.0.1:5000",
//   timeout: 5000,
//   headers: {'Content-Type': 'application/json'}
// });

/* eslint-disable no-new */
new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
