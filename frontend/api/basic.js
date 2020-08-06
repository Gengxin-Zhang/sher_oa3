export default $axios => ({
  signin() {
    return $axios.get('/sign/do')
  },
  mySigns() {
    return $axios.get('/sign/ls')
  },
  exportSigns() {
    return $axios.get('/sign/export')
  },
  initRoutine(signtime) {
    return $axios.post('/routine/init', signtime)
  },
  allRoutine() {
    return $axios.get('/routine/ls')
  },
  myRoutine() {
    return $axios.get('/routine/my')
  }
})
