<template>
    <div class="h-screen bg-gray-100">
        <l-map ref="map" :zoom="zoom" :center="[48.1117105, -1.6802281]">
            <l-tile-layer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                layer-type="base"
                name="OpenStreetMap"
            ></l-tile-layer>
            <l-marker v-for="marker in reviews" :key="marker.id" :lat-lng="[marker.latitude, marker.longitude]">
                <l-popup>
                    <div>
                        <strong>Nom:</strong>{{ marker.bar_name }}<br />
                        <strong>Note:</strong> {{ marker.note }} / 5 <br />
                        <strong>Prix de la bière:</strong> {{ marker.beer_price }} €
                    </div>
                </l-popup>
            </l-marker>
            <button @click="refreshMap">Refresh Map</button>
        </l-map>
    </div>
</template>

<script>
import 'leaflet/dist/leaflet.css';
import { LMap, LTileLayer, LMarker, LPopup } from '@vue-leaflet/vue-leaflet';
import { getReviews } from '@/services/reviews.service.js';

export default {
    components: {
        LMap,
        LTileLayer,
        LMarker,
        LPopup,
    },
    data() {
        return {
            zoom: 13,
        };
    },
    async created() {
        this.reviews = await getReviews();
    },
    async mounted() {
        await this.$nextTick();
        if (this.$refs.map.mapObject) {
            this.$refs.map.mapObject.invalidateSize();
        }
    },
    methods: {},
};
</script>
