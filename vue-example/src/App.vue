<script>
import axios from 'axios'
import Question from './components/Question.vue'

export default {
    components: {
        Question
    },
    data() {
        return {
            questions: []
        }
    },
    mounted () {
        axios.get('/api').then(response => (this.questions = response.data.data));
    }
}

//const questions = [1, 2, 3];
</script>

<template>
    <div v-for="question in questions">
        <Question :item="question" />
    </div>
</template>

<style>
</style>
