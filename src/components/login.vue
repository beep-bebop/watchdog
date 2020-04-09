<template>
    <div>
        <div class="login-wrap" v-show="showLogin">
            <h3>登陆</h3>
            <p v-show="showTishi">{{tishi}}</p>
            <input type="text" placeholder="请输入用户名" v-model="username"/>
            <input type="password" placeholder="请输入密码" v-model="password"/>
            <button v-on:click="login">登入</button>
            <span v-on:click="ToRegister">没有账号?马上注册</span>
        </div>
        <div class='register-wrap' v-show="showRegister">
            <h3>注册</h3>
            <p v-show="showTishi">{{tishi}}</p>
            <input type="text" placeholder="请输入用户名" v-model="newUsername"/>
            <input type="text" placeholder="请输入密码" v-model="newPassword" />
            <input type="text" placeholder="请输入手机号" v-model="newPhonenum" />
            <input type="text" placeholder="请输入宿舍楼号码" v-model="newDorm" />
            <input type="text" placeholder="请输入寝室号码" v-model="newRoom" />
            <button v-on:click="register">注册</button>
            <span v-on:click="ToLogin">已有账号?马上登入</span>
        </div>
    </div>
</template>

<script>
    import {setCookie,getCookie} from '../assets/js/cookie.js'
    export default{
        data(){
            return{
                username: '',
                password: '',
                newUsername: '',
                newPassword: '',
                newPhonenum: '',
                newDorm: '',
                newRoom: '',
                tishi: '',
                showTishi: false,
                showLogin: true,
                showRegister: false
            }
        },
        mounted(){
            if(getCookie("username")){
                this.$router.push('/')
            }
        },
        methods:{
            login(){
                if(this.username==""||this.password==""){
                    alert("请输入用户名或者密码")
                }else{
                    let params = new URLSearchParams();
                    params.append('username', this.username);
                    params.append('password', this.password);
                    this.$axios.post("http://127.0.0.1:5000/api/login",params).then((res)=>{
                        console.log(res.data)
                        console.log(typeof res.data)
                        if(res.data==-1){
//                          alert("aaaaa")
                            this.tishi = " 该用户不存在"
                            this.showTishi = true
                        }else if(res.data == 0){
                            this.tishi = "密码输入错误"
                            this.showTishi = true
                        }else if(res.data == "admin"){
                            this.$router.push("/main")
                        }else{
                            this.tishi = "登入成功"
                            this.showTishi = true
                            setCookie("username",this.username,1000*60)
                            setTimeout(function(){
                                this.$router.push("/")
                            }.bind(this),1000)
                        }
                    })
                }
            },
            ToRegister(){
                this.showRegister = true
                this.showLogin = false
            },
            ToLogin(){
                this.showRegister = false
                this.showLogin = true
            },
            register(){
                if(this.newUsername==""||this.newPassword==""){
                    alert("请输入用户名或者密码")
                }else{
                    let params = new URLSearchParams();
                    params.append('username', this.newUsername);
                    params.append('password', this.newPassword);
                    params.append('phonenum', this.newPhonenum);
                    params.append('dorm', this.newDorm);
                    params.append('room', this.newRoom);
                    this.$axios.post("http://127.0.0.1:5000/api/register",params).then((res)=>{
                        console.log(res)
                        console.log(res.data)
                        if(res.data== 1){
                            this.tishi = "注册成功"
                            this.showTishi = true
                            this.newUsername=""
                            this.newPassword=""
                            setTimeout(function(){
                                this.showRegister = false
                                this.showLogin = true
                                this.showTishi = false
                            }.bind(this),1000)
                        }
                    })
                }
            }

        }
    }
</script>

<style>
    .login-wrap{text-align:center;}
    input{display:block; width:250px; height:40px; line-height:40px; margin:0 auto; margin-bottom: 10px; outline:none; border:1px solid #888; padding:10px; box-sizing:border-box;}
    p{color:red;}
    button{display:block; width:250px; height:40px; line-height: 40px; margin:0 auto; border:none; background-color:#41b883; color:#fff; font-size:16px; margin-bottom:5px;}
    span{cursor:pointer;}
    span:hover{color:#41b883;}
</style>