<template>
    <div class="quote">

    <p class="text">
        {{ text }}
    </p>
    <p class="author">
        {{ author }}
    </p>

    </div>
    
</template>
<script>
    export default {
        name: "Quote",
        props: {
            text: {
                type: String,
                required: true,
            },
            author: {
                type: String,
                required: true,
            },
        },
    }
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:ital,wght@0,600;1,400&display=swap');
    .quote {
        margin: auto;
        margin-top: 3rem;
        display: block;
        width: 45%;
        min-height: 120px;
        padding: 1.5rem;
        background-color: white;
        border: none;
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.4);
        border-radius: 3px;
        font-family: 'Roboto Mono', monospace;
        position: relative;
     
    }
    .text{
        text-align:justify;
        font-style: oblique;
    }
    .author{
        bottom: 0;
        position: absolute;
        right: 5%;
        font-weight: bold;
        
    }
</style>