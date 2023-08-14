<template>
    <div class="h-screen bg-gray-100">
        <l-map ref="map" :zoom="zoom" :center="[48.1117105, -1.6802281]">
            <l-tile-layer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                layer-type="base"
                name="OpenStreetMap"
            ></l-tile-layer>
            <l-marker v-for="marker in markers" :key="marker.id" :lat-lng="[marker.latitude, marker.longitude]">
                <l-popup>
                    <div>
                        <strong>Nom:</strong>{{ marker.name }}<br />
                        <strong>Note:</strong> {{ marker.note }}<br />
                        <strong>Prix de la bière:</strong> {{ marker.beer_price }}
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
        this.markers = await this.fetchMarkers();
    },
    async mounted() {
        await this.$nextTick();
        if (this.$refs.map.mapObject) {
            this.$refs.map.mapObject.invalidateSize();
        }
    },
    methods: {
        async fetchMarkers() {
            try {
                const response = await fetch('http://127.0.0.1:5000/markers');
                if (!response.ok) {
                    throw new Error('Erreur lors de la récupération des marqueurs');
                }
                const markersData = await response.json();
                return markersData;
            } catch (error) {
                console.error('Erreur:', error);
            }
        },
    },
};
</script>
