<template>
	<view class="all">
		<view class="item" v-for="(item,index) in array">
			{{item}}
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				array:["吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码"],
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
</style>