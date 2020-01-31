<template>
  <div class="home">
     <HelloWorld msg="Welcome to Your Task Track App" />
    <div class="wrapper">
  
    <button class="button" @click="start()">Let's Start</button>

</div>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "login",
  components: {
    HelloWorld
  },
  methods: {
    start(){
    this.$router.push('login')
    }
  },
};
</script>
<style scoped>
.wrapper {
    text-align: center;
}

.button {
    position: absolute;
    top: 50%;
    height: 30px;
}
</style>