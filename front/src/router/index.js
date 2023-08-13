import { createRouter, createWebHistory } from "vue-router";
import LeafletMap from "@/components/LeafletMap.vue";
import MarkerForm from "@/components/MarkerForm.vue";

const routes = [
  {
    path: "/",
    name: "LeafletMap",
    component: LeafletMap,
  },
  {
    path: "/marker-form",
    name: "MarkerForm",
    component: MarkerForm,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;