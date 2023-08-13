<template>
    <div>
      <div>
        <label for="latitude">Latitude:</label>
        <input v-model="latitude" type="text" id="latitude" />
      </div>
      <div>
        <label for="longitude">Longitude:</label>
        <input v-model="longitude" type="text" id="longitude" />
      </div>
      <div>
        <label for="note">Note pour le bar:</label>
        <input v-model="note" type="text" id="note" />
      </div>
      <div>
        <label for="beerPrice">Prix de la bière le moins cher:</label>
        <input v-model="beerPrice" type="text" id="beerPrice" />
      </div>
      <button @click="addMarker">Ajouter le marqueur</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        latitude: "",
        longitude: "",
        note: "",
        beerPrice: "",
      };
    },
    methods: {
      addMarker() {
        if (this.latitude && this.longitude && this.note && this.beerPrice) {
          const markerData = {
            latitude: parseFloat(this.latitude),
            longitude: parseFloat(this.longitude),
            note: this.note,
            beerPrice: parseFloat(this.beerPrice),
          };
          this.$emit("markerAdded", markerData);
          this.latitude = "";
          this.longitude = "";
          this.note = "";
          this.beerPrice = "";
        } else {
          alert("Veuillez remplir tous les champs du formulaire.");
        }
      },
    },
  };
  </script>
  