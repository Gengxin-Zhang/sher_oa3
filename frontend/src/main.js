// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import global_ from './components/global'
import axios from './plugins/axios'

import { DatePicker, Button, Menu, Icon, message, notification, Tabs, Table } from 'ant-design-vue'

import 'ant-design-vue/dist/antd.css'
Vue.use(DatePicker)
Vue.use(Button)
Vue.use(Menu)
Vue.use(Icon)
Vue.use(Table)
Vue.use(axios)
Vue.use(Tabs)

Vue.config.productionTip = false

Vue.prototype.$message = message
Vue.prototype.$notification = notification
Vue.prototype.GLOBAL = global_
/* eslint-disable no-new */

router.beforeEach((to, from, next) => {
  console.log(from, to)
  if (to.matched.some(record => record.meta.permission !== undefined &&
                      record.meta.permission > store.getters.getPermission)) {
    // this route requires auth, check if logged in
    // if not, redirect to login page.
    // next({
    //   path: '/signin',
    //   query: { redirect: to.fullPath }
    // })
    next()
  } else {
    next() // 确保一定要调用 next()
  }
})

new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
