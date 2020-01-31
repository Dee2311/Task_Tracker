
<template>
  <div class="login-wr">

  
    <h2>Login Form</h2>


<div class="body"></div>
		<div class="grad"></div>
		<div class="header">
			<div style="font-weight:bold;font-size:40px;">Task<span>Tracker</span></div>
		</div>
		<br>
		<div class="login">
      
      <form @submit.prevent>
				<input type="text" placeholder="username" name="user" v-model="username"><br>
				<input type="password" placeholder="password" name="password" v-model="password"><br>
				<input type="button" @click="login()" value="Login">
        </form>
		</div>
  </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';

export default {

  name: 'LoginForm',
  template: '#login-form',
  data() {
    return {
      
      username: '',
      password: '',
    };
  },
  
  methods: {

    login: function () {
      // alert(`${this.username} ${this.password} ${this.rememberMe}`);

        let username = "dee",password = "2311";
        if(username == "dee" && password=="2311"){
          alert("Sucessfully Login");
          this.$router.push('list')

          console.log("logged in");
        }
        else{
          console.log("wrong Password")
        }
    /*
    isRememberMe() {
      return this.rememberMe === true;
    },

    login() {
      // we should handle errors in a more scalabe way, but this works for now

      alert(`${this.username} ${this.password} ${this.rememberMe}`);

      axios
        .post('http://127.0.0.1:8000/api/login/', {
          body: {
            username: this.username,
            password: this.password,
          },
        })
        .then((response) => {
          alert(response);
          // handle response and save JWT
        })
        .catch((err) => {
          alert(err);
        });
    },
    */
  },
}
}
</script>

<style scoped>
@import url(https://fonts.googleapis.com/css?family=Exo:100,200,400);
@import url(https://fonts.googleapis.com/css?family=Source+Sans+Pro:700,400,300);

body{
	margin: 0;
	padding: 0;
	background: #fff;

	color: #fff;
	font-family: Arial;
	font-size: 12px;
}

.body{
	position: absolute;
	top: -20px;
	left: -20px;
	right: -40px;
	bottom: -40px;
	width: auto;
	height: auto;
	background-image: url(http://ginva.com/wp-content/uploads/2012/07/city-skyline-wallpapers-008.jpg);
	background-size: cover;
	-webkit-filter: blur(5px);
	z-index: 0;
}

.grad{
	position: absolute;
	top: -20px;
	left: -20px;
	right: -40px;
	bottom: -40px;
	width: auto;
	height: auto;
	background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,rgba(0,0,0,0)), color-stop(100%,rgba(0,0,0,0.65))); /* Chrome,Safari4+ */
	z-index: 1;
	opacity: 0.7;
}

.header{
	position: absolute;
	top: calc(50% - 35px);
	left: calc(50% - 255px);
	z-index: 2;
}

.header div{
	float: left;
	color: #fff;
	font-family: 'Exo', sans-serif;
	font-size: 35px;
	font-weight: 200;
}

.header div span{
	color: #5379fa !important;
}

.login{
	position: absolute;
	top: calc(50% - 75px);
	left: calc(50% - 50px);
	height: 150px;
	width: 350px;
	padding: 10px;
	z-index: 2;
}

.login input[type=text]{
	width: 250px;
	height: 30px;
	background: transparent;
	border: 1px solid rgba(255,255,255,0.6);
	border-radius: 2px;
	color: #fff;
	font-family: 'Exo', sans-serif;
	font-size: 16px;
	font-weight: 400;
	padding: 4px;
}

.login input[type=password]{
	width: 250px;
	height: 30px;
	background: transparent;
	border: 1px solid rgba(255,255,255,0.6);
	border-radius: 2px;
	color: #fff;
	font-family: 'Exo', sans-serif;
	font-size: 16px;
	font-weight: 400;
	padding: 4px;
	margin-top: 10px;
}

.login input[type=button]{
	width: 260px;
	height: 35px;
	background: #fff;
	border: 1px solid #fff;
	cursor: pointer;
	border-radius: 2px;
	color: #a18d6c;
	font-family: 'Exo', sans-serif;
	font-size: 16px;
	font-weight: 400;
	padding: 6px;
	margin-top: 10px;
}

.login input[type=button]:hover{
	opacity: 0.8;
}

.login input[type=button]:active{
	opacity: 0.6;
}

.login input[type=text]:focus{
	outline: none;
	border: 1px solid rgba(255,255,255,0.9);
}

.login input[type=password]:focus{
	outline: none;
	border: 1px solid rgba(255,255,255,0.9);
}

.login input[type=button]:focus{
	outline: none;
}

::-webkit-input-placeholder{
   color: rgba(255,255,255,0.6);
}

::-moz-input-placeholder{
   color: rgba(255,255,255,0.6);
}
</style>