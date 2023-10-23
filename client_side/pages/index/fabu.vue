<template>
	<view>
		<view class="title">
			<view class="title_detail">参赛项目</view>
		</view>
		<view class="sorts">
			<!-- <view class="sort_position"> -->
				<view class="sort_item" v-for="(item,index) in array">
					{{item}}
				<!-- </view> -->
			</view>
		</view>
		<view class="sorts">
			<!-- <view class="sort_position"> -->
				<view class="sort_item" v-for="(item,index) in array">
					{{item}}
				</view>
			<!-- </view> -->
		</view>
		<view class="title">
			<view class="title_detail">项目简介</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				array:["吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码"]
			}
		},
		onLoad() {
	
		},
		methods: {
			
		}
	}
</script>

<style>
	.title{
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		background-color: antiquewhite;
		height: 8vh;
		width: 80vw;
		margin-left: 10vw;
		justify-content: space-around;
		margin-top: 3vh;
	}
	.title_detail{
		
	}
	.sorts{
		display: flex;
		flex-wrap: wrap;
		align-items: center;
		justify-content: center;
		background-color: antiquewhite;
		width: 78vw;
		margin-left: 10vw;
		margin-top: 3vh;
		padding:10rpx;
	}
	.sort_item{
		height:5vh;
		width: 15vw;
	}
</style>