import Auth from "@/api/auth"

export default (context, inject) => {
  // Initialize API repositories
  const repositories = {
    auth: Auth(context.$axios),
  };
  inject("api", repositories);
};
