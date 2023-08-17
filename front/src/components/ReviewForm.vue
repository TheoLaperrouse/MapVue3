<template>
    <div class="flex flex-col items-center p-6 space-y-4">
        <div class="flex flex-col space-y-1">
            <label for="barName" class="text-lg font-semibold"> Nom du bar: </label>
            <input
                v-model="barName"
                type="text"
                id="barName"
                class="border rounded p-2 focus:outline-none focus:border-blue-500"
            />
        </div>
        <div class="flex flex-col space-y-1">
            <label for="latitude" class="text-lg font-semibold"> Latitude: </label>
            <input
                v-model="latitude"
                type="text"
                id="latitude"
                class="border rounded p-2 focus:outline-none focus:border-blue-500"
            />
        </div>
        <div class="flex flex-col space-y-1">
            <label for="longitude" class="text-lg font-semibold"> Longitude: </label>
            <input
                v-model="longitude"
                type="text"
                id="longitude"
                class="border rounded p-2 focus:outline-none focus:border-blue-500"
            />
        </div>
        <div class="flex flex-col space-y-1">
            <label for="reviewer" class="text-lg font-semibold"> Votre prénom: </label>
            <input
                v-model="reviewer"
                type="text"
                id="reviewer"
                class="border rounded p-2 focus:outline-none focus:border-blue-500"
            />
        </div>
        <div class="flex flex-col space-y-1">
            <label for="note" class="text-lg font-semibold"> Note pour le bar: </label>
            <input
                v-model="note"
                type="text"
                id="note"
                class="border rounded p-2 focus:outline-none focus:border-blue-500"
            />
        </div>
        <div class="flex flex-col space-y-1">
            <label for="beerPrice" class="text-lg font-semibold"> Prix de la bière la moins chère: </label>
            <input
                v-model="beerPrice"
                type="text"
                id="beerPrice"
                class="border rounded p-2 focus:outline-none focus:border-blue-500"
            />
        </div>
        <button
            @click="addMarker"
            class="bg-blue-500 text-white font-semibold py-2 px-4 rounded hover:bg-blue-700 focus:outline-none focus:ring focus:ring-blue-300"
        >
            Ajouter le marqueur
        </button>
    </div>
</template>

<script>
import { postReview } from '@/services/reviews.service.js';

export default {
    data() {
        return {
            latitude: '',
            longitude: '',
            note: '',
            beerPrice: '',
            reviewer: '',
            barName: '',
        };
    },
    methods: {
        async addMarker() {
            if (this.latitude && this.longitude && this.note && this.beerPrice) {
                const markerData = {
                    latitude: parseFloat(this.latitude),
                    longitude: parseFloat(this.longitude),
                    note: this.note,
                    beer_price: parseFloat(this.beerPrice),
                    reviewer: this.reviewer,
                    barName: this.barName,
                };
                const response = await postReview(markerData);
                try {
                    if (response.ok) {
                        this.$router.push('/');
                        this.latitude = '';
                        this.longitude = '';
                        this.note = '';
                        this.beerPrice = '';
                        this.reviewer = '';
                        this.barName = '';
                    } else {
                        alert("Erreur lors de l'ajout du marqueur.");
                    }
                } catch (error) {
                    console.error('Erreur:', error);
                }
            } else {
                alert('Veuillez remplir tous les champs du formulaire.');
            }
        },
    },
};
</script>
