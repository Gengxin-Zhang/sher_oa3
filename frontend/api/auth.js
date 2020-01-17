export default ($axios) => ({
  signin(credentials) {
    return $axios.post("/auth/signin", credentials)
  },
  validToken(token) {
    return $axios.post("/auth/valid_token", {token})
  }
});
