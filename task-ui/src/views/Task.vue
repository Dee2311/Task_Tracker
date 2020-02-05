<template>
  <div class="createpost">
    
    <h1>Tasks</h1>
      <div class="TaskCard" v-for="task in tasks" :key="task.name">
         <div class="title"> 
           {{ task.title }}
         </div><hr>
         <div class="desc">
           {{ task.description }}
         </div><hr>
         <div class="exp">
           {{ task.expexted_time }}
         </div>
         <div class="due">
           {{ task.due_date }}
         </div><hr>
         <div class="status">
           {{ task.status }}
         </div>
       </div>       
          
      
 
  <div class="right">
    <input type="submit" style="width:100px;"  value="+ Add Task" class="new" @click="add()">
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
      tasks:[
       {
         "id":"1",
         "title":"Learning",
         "description":"To explore new thing",
         "expexted_time":"04:45",
         "due_date":"02-04-2020",
         "status":"Pending"
       },
        {
         "id":"2",
         "title":"Processing",
         "description":"We need to do something",
         "expexted_time":"14:25",
         "due_date":"08-09-2020",
         "status":"Unassigned"
       },
        {
         "id":"3",
         "title":"Development",
         "description":"working progress",
         "expexted_time":"52:45",
         "due_date":"04-11-2020",
         "status":"Accepted"
       },
        {
         "id":"4",
         "title":"Stock",
         "description":"Give me some information",
         "expexted_time":"47:10",
         "due_date":"02-02-2019",
         "status":"Completed"
       }
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
      this.$router.push('addtask')
    }
  }
};
</script>

<style>
.TaskCard{
  width: 400px;
  height: 200px;
  border:3px solid black;
  background-color: aqua;
  font-size: 20px;
  text-align: center;
  margin-block-start: 5%;
}
.main{
  width: 100%;
  height: 100%;
}
.exp{
  float: left;
  width: 200px;
  height: 40px;


}
.due{
  float: left;
  margin-top: 5px;
  width: 200px;
  height: 40px;
}

</style>
