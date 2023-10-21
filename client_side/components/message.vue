<template>
	<view>
		<view class="message_sort">
			<view class="sort_text" @click="clicknotice">通知</view>
			<view class="sort_text">团队</view>
			<view class="sort_text">关注</view>
		</view>
		<view class="message_detail">
			<view class="message_item">
				消息
			</view>
			<view class="message_item">
				消息
			</view>
			<view class="message_item">
				消息
			</view>
			<view class="message_item">
				消息
			</view>
			<view class="message_item">
				消息
			</view>
			<view class="message_item">
				消息
			</view>
		</view>
	</view>
</template>

<script>
	export default{
		methods:{
			clicknotice(){
				uni.navigateTo({
					url:"/pages/index/notices"
				})
			}
		}
	}
</script>

<style>
	.message_sort{
		display: flex;
		align-items: center;
		background-color: aliceblue;
		width: 80vw;
		height:8vh;
		justify-content: space-around;
		margin-top: 2vh;
		margin-left: 10vw;
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