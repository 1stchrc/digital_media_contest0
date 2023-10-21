<template>
	<view>
		<image class="setting" src="/static/zhuye_jiahao.png"></image>
		<image class="myhead" src="/static/logo.png"></image>
		<view class="items">
			<view class="item-text">简历</view>
			<view class="item-text">收藏</view>
		</view>
		<view class="items2">
			<view class="item-text">关注</view>
			<view class="item-text">待办</view>
			<view class="item-text">评价</view>
		</view>
		<view class="tag_and_pingjia">
			<view class="tag">
				<view class="tag_detail">理工</view>
				<view class="tag_detail">竞赛</view>
				<view class="tag_detail">大佬</view>
				<view class="tag_detail">奖项多</view>
			</view>
			<view class="pingjia">
				<view class="zhuwangtu">
					蛛网图（暂时不会实现）
				</view>
			</view>
		</view>
	</view>
</template>

<script>
</script>

<style>
	.setting{
		position: fixed;
		width: 70rpx;
		height: 70rpx;
		top: 3vh;
		right: 3vw;
	}
	.myhead{
		position: fixed;
		border-radius: 50%;
		width:200rpx;
		height: 200rpx;
		top: 7vh;
		left: 37vw;
	}
	.items{
		display: flex;
		align-items: center;
		justify-content: space-around;
		width: 80vw;
		background-color: antiquewhite;
		height: 10vh;
		margin-left:10vw;
		margin-top:25vh;
	}
	.item-text{
		
	}
	.items2{
		display: flex;
		align-items: center;
		justify-content: space-around;
		width: 80vw;
		background-color: antiquewhite;
		height: 10vh;
		margin-left:10vw;
		margin-top:5vh;
	}
	.tag_and_pingjia{
		display: flex;
		align-items: center;
		justify-content: space-between;
		width: 80vw;
		height: 30vh;
		margin-top: 5vh;
		background-color: antiquewhite;
		margin-left: 10vw;
	}
	.tag{
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: space-around;
		background-color: aqua;
		height: 25vh;
		width: 35vw;
	}
	.tag_detail{
		
	}
	.pingjia{
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		background-color: aqua;
		height: 25vh;
		width: 35vw;
	}
	.zhuwangtu{
		margin: 3vw;
	}
</style>