<template>
	<div>
		<div>
			<NavMenu></NavMenu>
			<Breadcrumb id="Breadcrumb"></Breadcrumb>
			<Avatar id="Avatar"></Avatar>
			<el-divider id="divider1"></el-divider>
		</div>
		<div id="backgroudDiv">
			<div id="temhmiDiv">
				<el-card id="temCard">
					<p style="text-align: center">实时温度：50</p>
					<p style="text-align: center">历史最高温度：50</p>
				</el-card>
				<el-card id="hmiCard">
					<p style="text-align: center; font-family: 微软雅黑">实时湿度：50</p>
					<p style="text-align: center; font-family: 微软雅黑" >历史最高湿度：50</p>
				</el-card>
			</div>
			<div id="ChartDiv">
				<el-card id="Chart">
					<Chart></Chart>
				</el-card>
			</div>
		</div>
	</div>
</template>

<script>
	import NavMenu from '../../components/NavMenu.vue'
	import Breadcrumb from '../../components/Breadcrumb.vue'
	import Avatar from "../../components/Avatar";
	import Chart from "../../components/temhui/ChartReal";
	
	export default{
		components: {
		  	NavMenu,
		  	Breadcrumb,
			Avatar,
			Chart
		},
	}
</script>

<style>
	#Breadcrumb{
		margin-top: 20px;
		margin-left: 300px;
	}
	#divider1{
		width: 86%;
		margin-top: 11px;
		margin-left: 244px;
	}
	#Avatar {
		margin-left: 93%;
		margin-top: -27px;
	}
	#backgroudDiv{
		background-color: #eceef1;
		height: 710px;
		margin-top: -1.7%;
	}
	#ChartDiv{
		width: 70%;
		margin-left: 23%;
		margin-top: 17%;
		position: absolute;
	}
	#Chart{
		width: 100%;
	}
	#temCard{
		width: 30%;
		margin-left: 23%;
		margin-top: 3%;
		float: left;
		background-color: #ffffff;
	}
	#hmiCard{
		width: 30%;
		margin-left: 63.8%;
		margin-top: -8.7%;
		float: left;
	}
</style>
