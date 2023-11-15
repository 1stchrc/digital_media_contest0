<template>
	<view class="login-all">
		<view class="title-all">
			<view class="title">欢迎登录TeamWork</view>
			<view class="title2">使用邮箱密码登录</view>
		</view>
		<input class="youxiang" type="text" v-model="mail" placeholder="邮箱" maxlength="64"></input>
		<input class="mima" type="safe-password" password="true" v-model="password" placeholder="密码" maxlength="64"></input>
		<view class="zhuce">没有账号？
		<view class="zhuce-gaoliang" @click="register()">注册</view>
		一个</view>
		<button class="botton" @click="confirm()">登录</button>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				mail : "",
				password : "",
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
				if(this.password === ""){
					uni.showToast({
						icon : "error",
						title : "密码不能为空",
						duration : 1000,
					});
					return;
				}
				try{
					await this.gd.logout();
					if(!(await this.gd.login({user_id : this.mail, password : this.password}))){
						uni.showToast({
							icon:"error",
							title:"邮箱或密码错误",
							duration:1000,
						})
						return;
					}
					uni.showToast({
						icon:"success",
						title:"登录成功",
						duration:1000,
					});
					
				} catch {
					uni.showToast({
						icon: "error",
						title: "无法连接到服务器",
						duration : 1000,
					});
				}
			},
			register(){
				uni.navigateTo({
					url:"./register"
				})
			}
		}
	}
</script>

<style>
	.login-all{
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
		align-items: center;
	}
	.title{
		margin-top: 20vh;
		width: 76vw;
		font-size: 55rpx;
		font-weight: 600;
	}
	.title2{
		margin-top: 1.15vh;
		color: rgb(176,176,176);
	}
	.youxiang,.mima{
		margin-top: 5vh;
		color: rgb(212,212,214);
		border-bottom-style: ridge;
		border-color: rgb(250,250,250);
		width: 73vw;
	}
	.botton{
		margin-top: 10vw;
		width: 76vw;
		background-color: rgb(158,172,245);
		color: white;
	}
	.zhuce{
		display: flex;
		margin-top: 3vh;
		color:rgb(176,176,176);
		width: 76vw;
		margin-left: 28vh;
	}
	.zhuce-gaoliang{
		color:rgb(102, 123, 254);
	}
</style>
