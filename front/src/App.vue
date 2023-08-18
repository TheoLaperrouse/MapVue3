<template>
    <div>
        <nav class="bg-blue-500 p-4">
            <router-link to="/" class="text-white hover:text-gray-200 mx-4"> Carte </router-link>
            <router-link to="/review-form" class="text-white hover:text-gray-200 mx-4"> Formulaire Note </router-link>
            <router-link to="/reviews-list" class="text-white hover:text-gray-200 mx-4"> Liste Reviews </router-link>
        </nav>
        <router-view></router-view>
    </div>
</template>

<script>
export default {
    name: 'App',
};
</script>
