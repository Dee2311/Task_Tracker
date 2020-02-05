<template>
  <div>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons"
      rel="stylesheet">
    <h1>Lists</h1>

      <div class="listCard" v-for="list in lists" :key="list.name">
       <div class="main">
        <router-link to="/Task">
        
         {{list.listName}}   
           </router-link>
       </div>
      </div>
 
<div>
    <input type="submit" value="+ Add List" class="new" @click="add()">
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import Postcard from "@/components/Postcard.vue";

// import axios from "axios";

export default {
  name: "list",
data () {
    return {
      lists:[
        {"id": 1, "listName": "Structure"},
       {"id": 2, "listName": "deepak "},
       {"id": 3, "listName": "Product"}, 
       {"id": 4, "listName": "Finally"}, 
       {"id": 5, "listName": "Project"}, 
       {"id": 6, "listName": "rest"}, 
       {"id": 7, "listName": "today"}
       ]
    }
},

  methods: {
    // mounted () 
    //   {
    //     axios.get("http://127.0.0.1:8000/Task/api/list").then(response => {
    //       this.list = response;
    //       console.log(this.list, "getting data from api");
    //       this.$router.push("/addList");
    //     })
    //     .catch(error => {
    //     console.log(error)
    //   })
    //   }
    // }
    add(){
      this.$router.push('addlist')
    }
  }
};
</script>

<style>
.listCard{
  width: 10px;
  /* height: 50px; */
  /* border:3px solid blue; */
}
.main{
  width: 100%;
  /* background-color: black; */
  
  padding: 10px;
  height: 100%;
}


</style>
