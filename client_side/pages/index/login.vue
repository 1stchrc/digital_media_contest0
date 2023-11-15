<template>
	<view>
		<input type="text" v-model="mail" placeholder="邮箱" maxlength="64"></input>
		<input type="safe-password" password="true" v-model="password" placeholder="密码" maxlength="64"></input>
		<button @click="confirm()">AAS</button>
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
					uni.navigateTo({
						url:"/pages/index/main",
					})
				} catch {
					uni.showToast({
						icon: "error",
						title: "无法连接到服务器",
						duration : 1000,
					});
				}
			},
		}
	}
</script>

<style>

</style>
