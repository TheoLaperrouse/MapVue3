<template>
    <div class="p-4">
        <h2 class="text-xl font-semibold mb-4">Liste des Marqueurs</h2>
        <ul class="space-y-2">
            <li v-for="mark in marks" :key="mark.id" class="border p-2">
                <p>Nom du bar: {{ mark.barName }}</p>
                <p>Latitude: {{ mark.latitude }}</p>
                <p>Longitude: {{ mark.longitude }}</p>
                <p>Note: {{ mark.note }}</p>
                <p>Prix de la bière: {{ mark.beerPrice }}</p>
                <p>Noteur: {{ mark.reviewer }}</p>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    props: {
        marks: Array, // Propriété pour passer la liste des marqueurs au composant
    },
    created() {},
};
</script>

<style scoped>
/* Utilisez des classes Tailwind CSS ici si nécessaire */
</style>
