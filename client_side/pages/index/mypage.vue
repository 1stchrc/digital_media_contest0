<template>
	<view class="mypage-all" style="background-color: rgb(244,244,244);">
		<view class="myhead">
			<view class="head-name">
				<image class="head-image" src="/static/logo.png"></image>
				<view class="user-id">用户名</view>
			</view>
			<view class="head-details">
				<view class="user-detail-item" style="border-right-style: solid;border-width: 2rpx;border-color: rgb(177,178,182);">
					<view class="user-detail-item-number">12</view>
					<view class="user-detail-item-text">简历</view>
				</view>
				<view class="user-detail-item">
					<view class="user-detail-item-number">12</view>
					<view class="user-detail-item-text">收藏</view>
				</view>
			</view>
		</view>
		<view class="items2">
			<view class="item2-text">关注</view>
			<view class="item2-text">评价</view>
		</view>
		
		<view class="items3">
			<view class="items3-each items3-border">
				<view class="tag">
					<view class="tag_detail">理工</view>
					<view class="tag_detail">竞赛</view>
					<view class="tag_detail">大佬</view>
					<view class="tag_detail">奖项多</view>
				</view>
			</view>
			<view class="items3-each">
				<view class="pingjia">
					<image class="pingjia-image" src="/static/add.png"></image>
					<view class="pingfen">
						评分
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default{
		data(){
			return{
				tanchuang:0
			}
		},
		methods:{
			clicktanchuang(){
				this.tanchuang=!this.tanchuang
			}
		}
	}
</script>

<style>
	.mypage-all{
		display: flex;
		flex-direction: column;
		align-items: center;
		padding-bottom: 15vh;
	}
	.tanchuang-each{
		display: flex;
		justify-content: center;
		align-items: center;
		width: 20vw;
		height: 6vh;
	}
	.tanchuang-each-border{
		border-bottom-style: solid;
		border-width: 2rpx;
		border-color: rgb(177,178,182);
	}
	.myhead{
		display: flex;
		flex-direction: column;
		justify-content: space-around;
		align-items: center;
		background-color: white;
		width:90vw;
		height: 30vh;
		margin-top: 3vh;
		border-bottom-left-radius: 20rpx;
		border-bottom-right-radius: 20rpx;
		box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.10);
	}
	.head-name{
		display: flex;
		/* justify-content: center; */
		align-items: center;
		/* background-color: aqua; */
		width: 85vw;
		height: 13vh;
	}
	.head-image{
		width: 120rpx;
		height: 120rpx;
		border-radius: 50%;
		margin-left: 3vw;
	}
	.user-id{
		font-size: 50rpx;
		margin-left: 3vw;
	}
	.head-details{
		display: flex;
		justify-content: space-around;
		align-items: center;
		/* background-color: aquamarine; */
		width: 85vw;
		height: 13vh;
	}
	.user-detail-item{
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: space-around;
		/* background-color: aliceblue; */
		width: 42.5vw;
		height: 150rpx;
	}
	.user-detail-item-number{
		font-size: 60rpx;
	}
	.user-detail-item-text{
		font-size: 30rpx;
		color: rgb(177,178,182);
	}
	.items2{
		display: flex;
		justify-content: space-around;
		align-items: center;
		background-color: white;
		width:90vw;
		height: 10vh;
		margin-top: 4vh;
		border-radius: 20rpx;
		box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.10);
	}
	.item2-text{
		font-size: 30rpx;
		color: rgb(97, 98, 100);
	}
	.items3{
		display: flex;
		justify-content: space-around;
		align-items: center;
		background-color: white;
		width:90vw;
		height: 30vh;
		margin-top: 4vh;
		border-radius: 20rpx;
		box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.10);
	}
	.items3-each{
		width: 45vw;
		display: flex;
		justify-content: center;
		align-items: center;
	}
	.items3-border{
		border-right-style: solid;
		border-width: 2rpx;
		border-color: rgb(177,178,182);
	}
	.tag{
		display: flex;
		flex-wrap: wrap;
		align-items: center;
		justify-content: space-around;
		/* background-color: aqua; */
		/* border-style: solid; */
		height: 25vh;
		width: 35vw;
	}
	.tag_detail{
		font-size: 40rpx;
		margin: 10rpx;
	}
	.pingjia-image{
		width: 150rpx;
		height: 150rpx;
		
	}
	.pingjia{
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		/* border-style: solid; */
		/* background-color: aqua; */
		height: 25vh;
		width: 35vw;
	}
	.pingfen{
		margin: 3vw;
	}
</style>