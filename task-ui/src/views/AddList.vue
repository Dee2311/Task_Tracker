<template>
<div>
    <h1>Add your new list here</h1>
  <input
      type="text"
      placeholder="Enter list title"
      v-model="list"
    /><br /> 
    <button @click="addList()">+ Create List</button>
</div>
</template>
<script>
import axios from 'axios';
export default {
  name: 'list',
  data() {
    return {
      listName: ''
    };
  },
  
  methods: {

    addList() {
      // we should handle errors in a more scalabe way, but this works for now
      axios
        .post('http://127.0.0.1:8000/api/list/', {
          body: {
            listName: this.listName,
          },
        })
        .then((response) => {
           this.$router.push('list')
          
        })
        .catch((err) => {
          alert(err);
        });
    }
  },
}

</script>
