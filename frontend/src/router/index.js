import Vue from 'vue'
import Router from 'vue-router'

function mapRoutes (routers) {
  return routers.map(route => {
    return {
      ...route,
      component: () => import(`@/pages/${route.component}.vue`)
    }
  })
}

const routerOption = [
  { path: '/', name: 'home', component: 'Home', meta: { permission: 0 } },
  { path: '/signin', name: 'signin', component: 'Signin', meta: { permission: -999 } },
  { path: '/user', name: 'user', component: 'User', meta: { permission: 3 } },
  { path: '*', name: 'error', component: 'Error', meta: { permission: -999 } }
]

const routes = mapRoutes(routerOption)

Vue.use(Router)

export default new Router({
  routes,
  mode: 'history'
})
