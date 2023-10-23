<template>
	<view>
		<input type="text" v-model="username" placeholder="用户名"></input>
		<input type="text" v-model="password" placeholder="密码"></input>
		<input type="text" v-model="passwordAgain" placeholder="确认密码"></input>
		<button @click="confirm()">AAS</button>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				username : "",
				password : "",
				passwordAgain : "",
				gd : getApp().globalData,
			}
		},
		methods: {
			confirm(){
				this.gd.request({
					url : this.gd.serverURL + "/register/",
					method : "POST",
					data : {
						username : this.username,
						password : this.password
					}
				}).then((res)=>{
					switch(res.statusCode){
						case 200:{
							uni.showToast({
								icon:"success",
								title:"注册成功"
							})
							this.gd.timeout(500).then(()=>{
								uni.hideToast();
							});
						}
					}
				}, (res)=>{
					uni.showToast({
						icon: "error",
						title: "未成功连接到服务器"
					});
					this.gd.timeout(500).then(()=>{
						uni.hideToast();
					});
				});
			}
		}
	}
</script>

<style>

</style>
