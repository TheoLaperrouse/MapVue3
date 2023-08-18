<template>
    <div class="p-4">
        <h2 class="text-xl font-semibold mb-4">Liste des Notes</h2>
        <ul class="space-y-2">
            <li v-for="review in reviews" :key="review.id" class="border p-2">
                <p>Nom du bar: {{ review.bar_name }}</p>
                <p>Note: {{ review.note }}</p>
                <p>Prix de la bière: {{ review.beer_price }}</p>
                <p>Prénom: {{ review.reviewer }}</p>
                <p>Description: {{ review.description }}</p>
            </li>
        </ul>
    </div>
</template>

<script>
import { getReviews } from '@/services/reviews.service.js';

export default {
    data() {
        return {
            reviews: [],
        };
    },
    async created() {
        this.reviews = await getReviews();
    },
};
</script>

<style scoped>
/* Utilisez des classes Tailwind CSS ici si nécessaire */
</style>
