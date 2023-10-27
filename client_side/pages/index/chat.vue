<template>
	<view class="chat-all">
		<view class="left">
			<image class="user-picture" src="../../static/logo.png"></image>
			<view class="chat-duixiang">
				<image class="duixiang-image" src="../../static/logo.png"></image>
				<image class="duixiang-image" src="../../static/logo.png"></image>
				<image class="duixiang-image" src="../../static/logo.png"></image>
				<image class="duixiang-image" src="../../static/logo.png"></image>
				<image class="duixiang-image" src="../../static/logo.png"></image>
			</view>
		</view>
		<view class="right">
			<view class="richeng-tixing">
				<image class="daosanjiao" src="../../static/daosanjiao.png"></image>
				日程提醒
			</view>
			<view class="tixing-detail">
				<image class="richeng-image" src="../../static/richeng.png"></image>
				<view class="richeng-text">***</view>
				<view class="richeng-jindu">
					完成度90%
				</view>
			</view>
			<view class="xiaoxi">
				<image class="daosanjiao" src="../../static/daosanjiao.png"></image>
				消息
			</view>
			<view v-if="ismore==0" class="chat-box">
				
			</view>
			<view v-else class="chat-box chat-box-detail">
				
			</view>
			<view class="chat-shuru">
				<input class="chat-shurukuang" placeholder="请输入发送内容"/>
				<image class="chat-more" src="../../static/add.png" @click="clickmore()"></image>
			</view>
			<view class="more-detail" v-if="ismore==1">
				<image class="more-item" src="../../static/tupian.png"></image>
				<image class="more-item" src="../../static/wenjian.png"></image>
				<image class="more-item" src="../../static/shipin.png"></image>
			</view>
		</view>
	</view>
</template>

<script>
	export default{
		data(){
			return{
				ismore: 0
			}
		},
		methods:{
			clickmore(){
				this.ismore=!this.ismore
			}
		}
	}
</script>

<style>
	.chat-all{
		display: flex;
	}
	.left{
		display: flex;
		flex-direction: column;
		align-items: center;
		width: 17vw;
		height: 100vh;
		border-right-style: ridge;
		/* background-color: antiquewhite; */
	}
	.user-picture{
		border-radius: 50%;
		margin-top: 2vh;
		width: 120rpx;
		height: 120rpx;
	}
	.chat-duixiang{
		display: flex;
		flex-direction: column;
		align-items: center;
		border-top-style: ridge;
		margin-top: 1vh;
		width: 18vw;
	}
	.duixiang-image{
		width: 120rpx;
		height: 120rpx;
		margin-top: 1vh;
	}
	.right{
		display: flex;
		flex-direction: column;
		align-items: center;
		/* justify-content: center; */
		width: 83vw;
		height: 100vh;
		/* background-color: cadetblue; */
	}
	.richeng-tixing{
		display: flex;
		align-items: center;
		width: 83vw;
		height: 8vh;
		/* background-color: aliceblue; */
		font-size: 35rpx;
	}
	.daosanjiao{
		width: 30rpx;
		height: 30rpx;
		margin-left: 5vw;
		margin-right: 2vw;
		margin-top: 0.5vh;
	}
	.tixing-detail{
		display: flex;
		align-items: center;
		border-style: solid;
		border-radius: 20rpx;
		width: 65vw;
		height: 7vh;
		border-width: 2rpx;
		border-color: rgb(143,143,143);
		
	}
	.richeng-image{
		width: 50rpx;
		height: 50rpx;
		margin-left: 2vw;
		margin-right: 2vw;
	}
	.richeng-text{
		width: 30vw;
		/* font-size: 30rpx; */
	}
	.richeng-jindu{
		font-size: 30rpx;
		color: rgb(143,143,143);
	}
	.xiaoxi{
		width: 83vw;
		margin-top: 3vh;
	}
	.chat-box{
		width: 65vw;
		height: 62vh;
		border-style: solid;
		border-width: 2rpx;
		border-color: rgb(143,143,143);
		margin-top: 3vh;
		margin-bottom: 3vh;
		border-radius: 20rpx;
	}
	.chat-box-detail{
		height: 48vh;
	}
	.chat-shuru{
		display: flex;
		justify-content: space-around;
		align-items: center;
		width: 65vw;
		height: 6vh;
		/* border-style: solid; */
		margin-top: 1vh;
		/* border-radius: 20rpx; */
	}
	.chat-shurukuang{
		border-style: solid;
		border-width: 2rpx;
		border-color: rgb(143,143,143);
		border-radius: 20rpx;
		width: 53vw;
		height: 6vh;
	}
	.chat-more{
		width: 70rpx;
		height: 70rpx;
		border-radius: 50%;
		margin-left: 2vw;
	}
	.more-detail{
		display: flex;
		flex-wrap: wrap;
		justify-content: space-around;
		align-items: center;
		margin-top: 3vh;
		width: 66vw;
		height: 13vh;
		border-style: solid;
		border-radius: 20rpx;
		border-width: 2rpx;
		border-color: rgb(143,143,143);
		/* box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.35); */
		/* background-color: rgb(238, 238, 238); */
	}
	.more-item{
		width: 90rpx;
		height: 90rpx;
		/* border-style: solid;
		border-width: 2rpx;
		border-color: rgb(143,143,143); */
	}
</style>