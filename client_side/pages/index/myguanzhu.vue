<template>
	<view class="all">
		<view class="search-block">
			<view class="search-ico-wapper">
				<image src="/static/search.png" class="search-ico" mode="heightFix"></image>
			</view>
			<input type="text" value="" placeholder="点击输入搜索内容" class="search-text" maxlength="10" focus/>
		</view>
	</view>
</template>

<script>
</script>

<style>
	.all{
		display: flex;
		justify-content: center;
		
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