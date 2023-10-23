<template>
	<view>
		<input type="text" v-model="mail" placeholder="邮箱" maxlength="64"></input>
		<input type="text" v-model="username" placeholder="用户名" maxlength="64"></input>
		<input type="safe-password" password="true" v-model="password" placeholder="密码" maxlength="64"></input>
		<input type="safe-password" password="true" v-model="passwordAgain" placeholder="确认密码" maxlength="64"></input>
		<button @click="confirm()">AAS</button>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				mail : "",
				username : "",
				password : "",
				passwordAgain : "",
				gd : getApp().globalData,
			}
		},
		methods: {
			async confirm(){
				if(!/[^\s@]+@[^\s@]+.[^\s@]+$/.test(this.mail)){
					uni.showToast({
						icon : "error",
						title : "请填写有效邮箱",
						duration : 1000,
					});
					return;
				}
				if(this.username === ""){
					uni.showToast({
						icon : "error",
						title : "用户名不能为空",
						duration : 1000,
					});
					return;
				}
				if(this.password === ""){
					uni.showToast({
						icon : "error",
						title : "密码不能为空",
						duration : 1000,
					});
					return;
				}
				if(this.password !== this.passwordAgain){
					uni.showToast({
						icon : "error",
						title : "两次密码输入不一致",
						duration : 1000,
					});
					return;
				}
				try{
					let result = await uni.request({
						url : this.gd.serverURL + "/register/",
						method : "POST",
						data : {
							mail : this.mail,
							username : this.username,
							password : this.password,
						},
					});
					switch(result.statusCode){
						case 200:{
							uni.showToast({
								icon : "success",
								title : "注册成功",
								duration : 1000,
							});
							break;
						}
						case 403:{
							uni.showToast({
								icon : "error",
								title : "邮箱已被注册",
								duration : 1000,
							});
							break;
						}
						default:{
							uni.showToast({
								icon : "error",
								title : "未知错误",
								duration : 1000,
							});
							break;
						}
					}
				} catch {
					uni.showToast({
						icon: "error",
						title: "未成功连接到服务器",
						duration : 1000,
					});
				}
			},
		}
	}
</script>

<style>

</style>
