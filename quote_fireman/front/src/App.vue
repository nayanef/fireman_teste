<template>
  <div id="app">
  <div class="quotes">

      <Quote v-for="(quote, index) in quotes" :key="index"
            :text="quote.text" :author="quote.author"/>
    
    </div>


  </div>
</template>

<script>
import Quote from './components/Quote.vue';
import axios from 'axios';


export default {
 
  name: 'App',
  components: {
    Quote,
  },

  data() {
    return {
      quotes: {},
     
    };
  },
  methods: {
    
    loadQuotes: function() {
    
      axios.get('/api/quotes/').then(
        
        response => {
          this.quotes = response.data;       
        }
        ).catch(error => {
        console.log(error);
      });
    }, 
  },
  created() {
    
    this.loadQuotes();
  },
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
