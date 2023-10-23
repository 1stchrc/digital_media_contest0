<template>
	<view>
		<view class="sort_bar">
			<view class="sort_item">全部</view>
			<view class="sort_item">直播</view>
			<view class="sort_item">高赞</view>
			<view class="sort_item">脑洞</view>
			<view class="sort_item">电竞</view>
			<view class="sort_item">健康</view>
		</view>
		<view class="detail">
			<view class="detail_left">
				<view class="detail_left_item">
					123
				</view>
				<view class="detail_left_item">
					123
				</view>
				<view class="detail_left_item">
					123
				</view>
				<view class="detail_left_item">
					123
				</view>
			</view>
			<view class="detail_right">
				<view class="detail_right_item">
					123
				</view>
				<view class="detail_right_item">
					123
				</view>
				<view class="detail_right_item">
					123
				</view>
			</view>
		</view>
		<image class="add" src="../../static/add.png"></image>
	</view>
</template>

<script>
</script>

<style>
	.sort_bar{
		display: flex;
		align-items: center;
		justify-content: space-around;
		background-color: antiquewhite;
		width: 100vw;
		height: 5vh;
	}
	.sort_item{
		
	}
	.detail{
		display: flex;
		align-items: center;
		justify-content: center;
		margin-top:3vh;
	}
	.detail_left{
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: space-around;
		width: 50vw;
		background-color: antiquewhite;
	}
	.detail_right{
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: space-around;
		width: 50vw;
		background-color: antiquewhite;
	}
	.detail_left_item{
		height: 5vh;
		width: 40vw;
		background-color: aqua;
	}
	.detail_right_item{
		height: 7vh;
		width: 40vw;
		background-color: aqua;
	}
	.add{
		position: fixed;
		width: 90rpx;
		height: 90rpx;
		right: 10vw;
		bottom: 5vh;
	}
</style>