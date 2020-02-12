<template>
  <div>
    <!-- <link
      href="https://fonts.googleapis.com/icon?family=Material+Icons"
      rel="stylesheet"
    /> -->
    <h1>Lists</h1>

    <div class="listCard" v-for="list in lists" :key="list.name">
       <div class="main">
        <router-link to="/Task">
        
         {{list.listName}}   
           </router-link>
       </div>
      </div>

    <div>
      <input type="submit" value="+ Add List" class="new" @click="add()" />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import Postcard from "@/components/Postcard.vue";

import axios from "axios";

export default {
  name: "list",
  data() {
    return {
      lists: null
    };
  },
    mounted() {
      axios.get("http://127.0.0.1:8000/api/viewList/").then(response => {
        this.lists = response.data;
      });
      
    },
    methods: {
      add(){
      this.$router.push('addlist')
    }
    },
    }
    
</script>

<style>
.listCard {
  width: 10px;
  /* height: 50px; */
  /* border:3px solid blue; */
}
.main {
  width: 100%;
  /* background-color: black; */
  padding: 10px;
  height: 100%;
}
</style>
