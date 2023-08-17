import { createRouter, createWebHistory } from 'vue-router';
import LeafletMap from '@/components/LeafletMap.vue';
import ReviewForm from '@/components/ReviewForm.vue';
import ReviewsList from '@/components/ReviewsList.vue';

const routes = [
    {
        path: '/',
        name: 'LeafletMap',
        component: LeafletMap,
    },
    {
        path: '/review-form',
        name: 'ReviewForm',
        component: ReviewForm,
    },
    {
        path: '/reviews-list',
        name: 'ReviewsList',
        component: ReviewsList,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
