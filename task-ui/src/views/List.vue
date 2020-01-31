<template>
  <div class="createpost">
    <h1>Lists</h1>

    <ul>
      <li v-for="lists in list" :key="lists.name">
        <i class="fas fa-list">{{ lists.listName }}</i>
      </li>
    </ul>

    <button @click="add()">+ New list</button>
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
      list: null
    };
  },
  methods: {
    mounted () {
      {
        axios.get("http://127.0.0.1:8000/Task/api/list").then(response => {
          this.list = response;
          console.log(this.list, "getting data from api");
          this.$router.push("/addList");
        })
        .catch(error => {
        console.log(error)
      })
      }
    },
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
