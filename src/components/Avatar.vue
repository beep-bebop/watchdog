<template>
	 <div id="avatar">
	      <el-avatar :src="url" :size="35" class="bg"></el-avatar>
		  <el-dropdown @command="handleCommand">
		    <span class="el-dropdown-link">
		      {{ username }}
				<i class="el-icon-arrow-down el-icon--right"></i>
		    </span>
		    <el-dropdown-menu slot="dropdown">
		      <el-dropdown-item command="info">个人信息</el-dropdown-item>
		      <el-dropdown-item command="pass">修改密码</el-dropdown-item>
		      <el-dropdown-item divided command="log-out">退出登录</el-dropdown-item>
		    </el-dropdown-menu>
		  </el-dropdown>
	</div>
</template>

<script>
import bgurl from "../assets/images/login.jpg"
import {getCookie} from "../cookie.js"
export default {
	name:'Avatar',
	data(){
		return{
			//username: getCookie("username"),
			username: "zgy",
			url: bgurl,
		};
	},
    methods: {
      handleCommand(command) {
        if(command == "info"){
			this.$router.replace('/personal')
			console.log("个人信息")
		}
      }
    }
  }
</script>

<style>
#avatar .el-dropdown-link {
    cursor: pointer;
    color: #409EFF;
	font-size: 0.9375rem;
}
#avatar .el-icon-arrow-down {
    font-size: 12px;
}
#avatar .bg{
	margin: 0px 10px -10px;
}
</style>
