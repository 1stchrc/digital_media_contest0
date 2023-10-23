<template>
	<view style="padding-top: 2vh;background-color: rgb(244,244,244);">
		<view class="message_sort">
			<view class="sort_text" @click="clicknotice">通知</view>
			<view class="sort_text" @click="clicktuandui">团队</view>
			<view class="sort_text" @click="clickguanzhu">关注</view>
		</view>
		<view class="all">
			<view class="item" v-for="(item,index) in array">
				{{item}}
			</view>
		</view>
	</view>
</template>

<script>
	export default{
		data() {
			return {
				array:["吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码"],
			}
		},
		methods:{
			clicknotice(){
				uni.navigateTo({
					url:"/pages/index/notices"
				})
			},
			clicktuandui(){
				uni.navigateTo({
					url:"/pages/index/myteam"
				})
			},
			clickguanzhu(){
				uni.navigateTo({
					url:"/pages/index/myguanzhu"
				})
			}
		}
	}
</script>

<style>
	.all{
		display: flex;
		flex-direction: column;
		background-color: rgb(244,244,244);
		height: fit-content;
		overflow-y: auto;
		align-items: center;
	}
	.item{
		display: flex;
		background-color: rgb(255,255,255);
		width: 80vw;
		box-shadow: 0px 0px 5px 0px rgba(0, 0, 0, 0.2);
		margin-top:3vh;
		border-radius: 20rpx;
		justify-content: center;
		align-items: center;
		height: 10vh;
	}
	.message_sort{
		display: flex;
		align-items: center;
		background-color: aliceblue;
		width: 80vw;
		height:8vh;
		justify-content: space-around;
		margin-left: 10vw;
		box-shadow: 0px 0px 5px 0px rgba(0, 0, 0, 0.2);
	}
	.sort_text{
		
	}
	.message_detail{
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: space-around;
		width: 80vw;
		margin-top: 3vh;
		margin-left: 10vw;
		background-color: bisque;
		height:70vh;
	}
	.message_item{
		width: 78vw;
		background-color: aliceblue;
		border-style: ridge;
		height: 8vh;
	}
</style>