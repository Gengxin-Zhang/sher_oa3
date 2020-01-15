import Auth from "@/api/auth"

export default (context, inject) => {
  if (process.client) {
    const token = localStorage.getItem("token");
    // Set token when defined
    if (token) {
      context.$axios.setToken(token, "Bearer");
    }
  }
  // Initialize API repositories
  const repositories = {
    auth: Auth(context.$axios),
  };
  inject("api", repositories);
};
