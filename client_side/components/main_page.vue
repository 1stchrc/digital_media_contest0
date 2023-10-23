<template>
	<view class="all">
		<view class="sort_bar">
			<view class="sort_item">答疑</view>
			<view class="sort_item">经验分享</view>
		</view>
		<swiper class="swiper" indicator-dots='ture' autoplay="ture" interval=3000 circular="ture">
			<swiper-item><image class="swiper_image" src='/static/logo.png'></image></swiper-item>
			<swiper-item><image class="swiper_image" src='/static/logo.png'></image></swiper-item>
			<swiper-item><image class="swiper_image" src='/static/logo.png'></image></swiper-item>
		</swiper>
		
		<view class="search-block">
			<view class="search-ico-wapper">
				<image src="/static/search.png" class="search-ico" mode="heightFix"></image>
			</view>
			<input type="text" value="" placeholder="点击输入搜索内容" class="search-text" maxlength="10" focus/>
		</view>
		<view class="detail">
			<view class="detail_left">
				<view class="detail_left_item">
					讨论贴
				</view>
				<view class="detail_left_item">
					讨论贴
				</view>
				<view class="detail_left_item">
					讨论贴
				</view>
				<view class="detail_left_item">
					讨论贴
				</view>
			</view>
			<view class="detail_right">
				<view class="detail_right_item">
					讨论贴
				</view>
				<view class="detail_right_item">
					讨论贴
				</view>
				<view class="detail_right_item">
					讨论贴
				</view>
				<view class="detail_right_item">
					讨论贴
				</view>
				
			</view>
		</view>
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
	.all{
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	.swiper{
		margin-top:2vh;
		height: 30vh;
		width: 90vw;
		border-radius: 20rpx;
		box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.35)
	}
	.swiper_image{
		height: 30vh;
		width: 90vw;
	}
	
	.cansai_jingyan{
		margin-top: 5vw;
		width: 80vw;
		background-color: aliceblue;
		height: 100vh;
		overflow-y: auto;
	}
	.detail{
		display: flex;
		/* align-items: center; */
		justify-content: space-around;
		margin-top:3vh;
		width:99vw;
	}
	.detail_left{
		display: flex;
		flex-direction: column;
		width: 48vw;
		/* background-color: antiquewhite; */
	}
	.detail_right{
		display: flex;
		flex-direction: column;
		width: 48vw;
		/* background-color: antiquewhite; */
	}
	.detail_left_item{
		display: flex;
		justify-content: center;
		align-items: center;
		height: 15vh;
		width: 48vw;
		background-color: rgb(250,250,250);
		margin-top:1vh;
		border-radius: 20rpx;
		box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.10);
	}
	.detail_right_item{
		display: flex;
		justify-content: center;
		align-items: center;
		height: 17vh;
		width: 48vw;
		background-color: rgb(250,250,250);
		margin-top:1vh;
		border-radius: 20rpx;
		box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.10);
	}
	.search-text{
		font-size: 14px;
		background-color: transparent;
		height: 80%;
		width: 80vw;
	}
	.search-block{
		display: flex;
		flex-direction: row;
		position: relative;
		align-items: center;
		top: 20upx;
		background-color: rgb(250,250,250);
		border-radius: 2.5vh;
		height: 5vh;
		width: fit-content;
		box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.20);
	}
	.search-ico{
		margin-right: 2vw;
		height: 100%;
	}
	.search-ico-wapper{
		background-color: transparent;
		display: flex;
		justify-content: center;
		height: 90%;
		margin: 0upx 0upx 0upx 15upx;
	}
</style>