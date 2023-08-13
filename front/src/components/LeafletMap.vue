<template>
    <div class="h-screen bg-gray-100">
        <l-map ref="map" :zoom="zoom" :center="[48.1117105, -1.6802281]">
            <l-tile-layer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                layer-type="base"
                name="OpenStreetMap"
            ></l-tile-layer>
        </l-map>
    </div>
</template>

<script>
import 'leaflet/dist/leaflet.css';
import { LMap, LTileLayer } from '@vue-leaflet/vue-leaflet';

export default {
    components: {
        LMap,
        LTileLayer,
    },
    data() {
        return {
            zoom: 13,
        };
    },
    created() {
        this.markers = [];
    },
    methods: {
        async fetchMarkers() {
            try {
                const response = await fetch('/markers');
                if (!response.ok) {
                    throw new Error('Erreur lors de la récupération des marqueurs');
                }
                const markersData = await response.json();
                this.markers = markersData;
            } catch (error) {
                console.error('Erreur:', error);
            }
        },
    },
};
</script>
