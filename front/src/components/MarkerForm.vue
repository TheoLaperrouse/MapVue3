<template>
    <div class="flex flex-col items-center p-6 space-y-4">
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
export default {
    data() {
        return {
            latitude: '',
            longitude: '',
            note: '',
            beerPrice: '',
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
                };
                try {
                    const response = await fetch('http://localhost:5000/markers', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify(markerData),
                    });

                    if (response.ok) {
                        this.$router.push('/');
                        this.latitude = '';
                        this.longitude = '';
                        this.note = '';
                        this.beerPrice = '';
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
