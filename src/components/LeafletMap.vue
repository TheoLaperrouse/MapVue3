<template>
  <div class="h-screen bg-gray-100">
    <l-map ref="map" v-model:zoom="zoom" :center="[48.1117105,-1.6802281]">
      <l-tile-layer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        layer-type="base"
        name="OpenStreetMap"
      ></l-tile-layer>
    </l-map>
  </div>
</template>
  
  <script>
  import axios from 'axios'
  import "leaflet/dist/leaflet.css";
  import { LMap, LTileLayer } from "@vue-leaflet/vue-leaflet";
  
  export default {
    components: {
      LMap,
      LTileLayer,
    },
    data() {
      return {
        zoom: 15,
      };
    },
    created(){
      this.markers = []
    },
    methods:{
      async fetchMarkers() {
        try {
          const response = await axios.get('/get_markers'); // Utilisez l'URL correcte de votre API Flask
          const markers = response.data; // Liste des marqueurs au format JSON
          console.log(markers); // Faites quelque chose avec les marqueurs récupérés
        } catch (error) {
          console.error('Erreur lors de la récupération des marqueurs:', error);
        }
      }
    }
  };
  </script>
  
<style>
</style>