<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <router-link id="sensors" to="/sensors">sensors</router-link>
    <router-link id="login" to="/login">login</router-link>
    <h3>欢迎{{name}}</h3>
    <a href="/" v-on:click="quit">注销登入</a>
  </div>
</template>

<script>
  // eslint-disable-next-line no-unused-vars
  import {setCookie,getCookie,delCookie} from '../assets/js/cookie.js'
  export default{
    data(){
      return{
        name:""
      }
    },
    mounted(){
      let uname = getCookie("username")
      this.name = uname
      if(uname == ""){
        this.$router.push("/")
      }
    },
    methods:{
      quit(){
        delCookie("username")
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
