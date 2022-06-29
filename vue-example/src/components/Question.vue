<script>
export default {
    props: ['item'],
}
</script>

<template>
    <h2>{{ item.text }}</h2>
    <ul v-for="choice in item.choices">
        <li>{{ choice }}</li>
    </ul>
    <h3>{{ item.answer }}</h3>
    <div id="line"></div>
</template>

<style scoped>
    #line {
        border: black solid 2px;
    }
</style>
