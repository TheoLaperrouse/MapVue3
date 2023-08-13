import Vue from "vue";
import App from "./App.vue";
import VueRouter from "vue-router";
import LeafletMap from "./components/LeafletMap.vue";
import MarkerForm from "./components/MarkerForm.vue";

Vue.config.productionTip = false;

Vue.use(VueRouter);

const routes = [
  { path: "/", component: LeafletMap }, // Route pour la carte (composant de la carte)
  { path: "/marker-form", component: MarkerForm }, // Route pour un autre composant
];

const router = new VueRouter({
  routes,
});

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");