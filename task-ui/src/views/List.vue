<template>
  <div class="createpost">
    <h1>Lists</h1>

    <ul>
      <li v-for="list in lists" :key="list.name">
        <router-link to="/Task">
       <i class="fas fa-list">{{ list.listName }}</i>
       </router-link>
        
      </li>
    </ul>

    <button @click="add()">+ New list</button>
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
.createpost {
  width: 760px;
  margin: auto;
}
input {
  width: 100%;
  margin-bottom: 20px;
  padding: 10px 0;
}
textarea {
  width: 100%;
  height: 200px;
  margin-bottom: 20px;
}
</style>
