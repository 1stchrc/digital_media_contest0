<template>
	<view class="all">
		<view class="fanhui" @click="fanhui()"><</view>
		<view class="top">
			发布组队
		</view>
		<view class="bisai-zhaomu">
			* * * 比 赛 招 募
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		onLoad() {
	
		},
		methods: {
			fanhui(){
				uni.navigateTo({
					url:"/pages/index/main"
				})
			}
		}
	}
</script>

<style>
	.fanhui{
		position: fixed;
		left: 7vw;
		top:8vh;
		font-size: 50rpx;
	}
	.all{
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.top{
		display: flex;
		justify-content: center;
		align-items: center;
		/* background-color: beige; */
		width: 90vw;
		height: 8vh;
		border-bottom-style: ridge;
	}
	.bisai-zhaomu{
		width: 86vw;
		
	}
</style>