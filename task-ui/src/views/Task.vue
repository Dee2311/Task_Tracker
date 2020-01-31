<template>
  <div class="createpost">
    <h1>Task</h1>

    <div v-for="task in tasks" :key="task.id">
      <p class="fas fa-list">{{ task.title }}</p>
    </div>

    <button @click="add()">+ New Task</button>
  </div>
</template>

<script>
// @ is an alias to /src
// import Postcard from "@/components/Postcard.vue";

import axios from "axios";

export default {
  name: "home",

  data() {
    return {
      tasks: null
    };
  },
  methods: {
    mounted() {
      {
        axios
          .get("http://127.0.0.1:8000/Task/api/task")
          .then(response => {
            this.tasks = response;
            console.log(this.list, "getting data from api");
            this.$router.push("/addTask");
          })
          .catch(error => {
            console.log(error);
          });
      }
    },
    add() {
      this.$router.push("addtask");
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
