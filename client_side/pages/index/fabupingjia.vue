<template>
	<view class="all">
		<view class="fanhui" @click="fanhui()"><</view>
		<view class="top">
			评价
		</view>
		<view class="item-each">
			<view class="item-text">技术能力</view>
			<image class="stars" src="../../static/shoucang.png"></image>
			<image class="stars" src="../../static/shoucang.png"></image>
			<image class="stars" src="../../static/shoucang.png"></image>
			<image class="stars" src="../../static/shoucang.png"></image>
			<image class="stars" src="../../static/shoucang.png"></image>
			<input class="shuoming" placeholder="评价分数说明"/>
		</view>
		<view class="item-each">
			<view class="item-text">沟通能力</view>
			<image class="stars" src="../../static/shoucang.png"></image>
			<image class="stars" src="../../static/shoucang.png"></image>
			<image class="stars" src="../../static/shoucang.png"></image>
			<image class="stars" src="../../static/shoucang.png"></image>
			<image class="stars" src="../../static/shoucang.png"></image>
			<input class="shuoming" placeholder="评价分数说明"/>
		</view>
		<view class="item-each">
			<view class="item-text">合作态度</view>
			<image class="stars" src="../../static/shoucang.png"></image>
			<image class="stars" src="../../static/shoucang.png"></image>
			<image class="stars" src="../../static/shoucang.png"></image>
			<image class="stars" src="../../static/shoucang.png"></image>
			<image class="stars" src="../../static/shoucang.png"></image>
			<input class="shuoming" placeholder="评价分数说明"/>
		</view>
		<view class="item-each">
			<view class="item-text">诚信分</view>
			<image class="stars" src="../../static/shoucang.png"></image>
			<image class="stars" src="../../static/shoucang.png"></image>
			<image class="stars" src="../../static/shoucang.png"></image>
			<image class="stars" src="../../static/shoucang.png"></image>
			<image class="stars" src="../../static/shoucang.png"></image>
			<input class="shuoming" placeholder="评价分数说明"/>
		</view>
		<view class="bottom">
			<!-- <image class="cuncaogao" src="../../static/cuncaogao.png" @click="saveDraft()">草稿</image> -->
			<button class="fabu" @click="confirm()">发布</button>
		</view>
	</view>
</template>

<script>
	export default{
		methods: {
			fanhui(){
				uni.navigateTo({
					url:"/pages/index/main"
				})
			},
		},
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
		font-size: 40rpx;
	}
	.bottom{
		display: flex;
		align-items: center;
		position: fixed;
		bottom:2vh;
		width: 90vw;
		height: 8vh;
		border-top-style: ridge;
		/* background-color: aliceblue; */
	}
/* 	.cuncaogao{
		margin-left: 2vh;
		margin-right: 1vh;
		width:60rpx;
		height: 60rpx;	
	} */
	.fabu{
		display: flex;
		margin-left: 50vw;
		align-items: center;
		justify-content: center;
		width: 50vw;
		height: 5vh;
		border-radius: 50rpx;
		background-color: rgb(52,120,245);
		color:white;
		box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.35);
	}
	.stars{
		/* margin-top: 0vh; */
		width: 40rpx;
		height: 40rpx;
		margin-left: 30rpx;
	}
	.item-text{
		font-size: 40rpx;
		margin-top: -7rpx;
	}
	.item-each{
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
		align-items: center;
		margin-top: 5vh;
	}
	.shuoming{
		width: 65vw;
		border-style: ridge;
		margin-top: 3vh;
		padding: 6rpx;
		height: 4vh;
		border-radius: 20rpx;
	}
</style>