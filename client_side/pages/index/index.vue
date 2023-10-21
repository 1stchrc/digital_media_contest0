<template>
	<view class="content">
		<image class="logo" src="/static/logo.png"></image>
		<button class="confirm" @click="click_confirm">开始</button>
		<view class="text-area">
			<text class="title">******</text>
		</view>
		<view class="text-area">
			<text class="title">slogan</text>
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
			click_confirm(){
				uni.navigateTo({
					url:"/pages/index/main",
				})
			},
		}
	}
</script>

<style>
	.content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}

	.logo {
		height: 300rpx;
		width: 300rpx;
		margin-top: 300rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx;
	}

	.text-area {
		display: flex;
		justify-content: center;
	}

	.title {
		font-size: 36rpx;
		color: #8f8f94;
	}
</style>
