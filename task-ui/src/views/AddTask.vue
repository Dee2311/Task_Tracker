<template>
  <div class="main">
    <h1>Add Task</h1>
    <label>Title : </label>
    <input  placeholder="Enter the tittle"><br> 
    <label> Description : </label>
    <textarea  title="Description" placeholder="Enter your description here....."></textarea><br>
      <div class="left">
      <label>Expected Time : </label>
      <vue-timepicker format="HH:mm"></vue-timepicker>
      </div>
      <div class="right">
        <label>Due Date : </label>
       <datepicker placeholder="Enter the date"></datepicker>
     </div><br><br>

 <label>Status : </label>    
<select style="width:100px;">
  <!-- <option v-for="option in options" :key="option.value">
    {{ option.text }}
  </option> -->
        

  <option value="Unassigned">Unassigned</option>
  <option value="Accepted">Accepted</option>
  <option value="Completed">Completed</option>
  <option value="Pending">Pending</option>
  <option value="Started">Started</option>

</select>


  <br>

    <button @click="view()">+ AddTask</button> 
  </div>
</template>
<script>
import axios from 'axios';
import VueTimepicker from 'vue2-timepicker/src';

import Datepicker from 'vuejs-datepicker';
export default {
  name: "Task",
  components: { VueTimepicker, Datepicker  },
  data() {
    return {
      
      title: '',
      description: '',
      expected_time:'',
      due_date:'',
      status:'',
    };
  },
  
  methods: {

    addList() {
      // we should handle errors in a more scalabe way, but this works for now
      axios
        .post('http://127.0.0.1:8000/api/list/', {
          body: {
            listName: this.listName,
            description: this.description,
            expected_time: this.expected_time,
            due_date: this.due_date,
            status: this.status
          },
        })
        .then((response) => {
          alert(response);

           this.$router.push('task')
          
        })
        .catch((err) => {
          alert(err);
           this.$router.push('Task')

        });
    }
  },
}

</script>



<style>
.main {
  width: 100%;
  margin: auto;
}
input{
  padding: 10px;
  margin-bottom: 20px;
}
textarea{
  /* padding: 10px; */
  margin-top: 20px;
  ;
}

.left{
  float: left;
  width: 400px;
  height: 200px;
  /* background-color: aqua; */
}
.right{
  float: right;
  margin-top: 5px;
  text-align: start;
  width: 400px;
  height: 80px;
  /* background-color: blue; */
}
</style>
