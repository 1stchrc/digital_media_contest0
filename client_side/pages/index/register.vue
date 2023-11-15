<template>
	<view class="all">
		<view class="register-text">注册账号</view>
		<input class="input" type="text" v-model="mail" placeholder="请输入邮箱" maxlength="64"></input>
		<input class="input" type="text" v-model="username" placeholder="请输入用户名" maxlength="64"></input>
		<input class="input" type="safe-password" password="true" v-model="password" placeholder="密码" maxlength="64"></input>
		<input class="input" type="safe-password" password="true" v-model="passwordAgain" placeholder="确认密码" maxlength="64"></input>
		<button class="button" @click="confirm()">立即注册</button>
		<view class="login" @click="login()">已有账号，点此去登陆</view>
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
			login(){
				uni.navigateTo({
					url:"./login"
				})
			}
		}
	}
</script>

<style>
	.all{
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
		align-items: center;
	}
	.register-text{
		margin-top: 11vh;
		width: 76vw;
		font-size: 55rpx;
		font-weight: 500;
	}
	.input{
		width: 76vw;
		margin-top: 3vh;
		height: 7vh;
		border-radius: 50rpx;
		padding-left: 5vw;
		background-color: rgb(229,244,251);
	}
	.button{
		margin-top: 10vw;
		width: 76vw;
		background-color: rgb(158,172,245);
		color: white;
	}
	.login{
		display: flex;
		margin-top: 3vh;
		color:rgb(176,176,176);
	}
</style>
