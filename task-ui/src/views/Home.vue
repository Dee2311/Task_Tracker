<template>
  <div class="home">
     <HelloWorld msg="Welcome to Your Task Tracker App" />
    <div class="bg">
      <button class="start">Let's Start</button>
    </div>
   
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "home",
  components: {
    HelloWorld
  }
};
</script>
<style scoped>
body, html {
  height: 100%;
  margin: 0;
}

.bg {
  /* The image used */
  background-image: url("../assets/bg.jpg");

  /* Full height */
  height: 100%; 
  width: 100%;

  /* Center and scale the image nicely */
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
</style>