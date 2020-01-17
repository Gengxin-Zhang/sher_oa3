import Vue from "vue";

// PROJECT: COMMONS
import development from "@/config/development.json";
import production from "@/config/production.json";


export default (context, inject) => {
  if (process.env.NODE_ENV === "production") {
    inject("config", Object.freeze(production));
  } else {
    inject("config", Object.freeze(development))
  }
}
