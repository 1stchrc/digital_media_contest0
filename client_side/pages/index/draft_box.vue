<template>
	<view class="all">
		<view class="fanhui" @click="fanhui()"><</view>
		<view class="top">草稿箱</view>
		<view class="detail">
			<view class="detail_left">
				<view v-for="(e, i) in leftContents"
				:key="i"
				class="detail_left_item" @click="open_detail"
				>{{e.title}}
					<image class="delete" src="../../static/add.png"></image>
				</view>
			</view>
			<view class="detail_right">
				<view v-for="(e, i) in rightContents"
				:key="i"
				class="detail_right_item" @click="open_detail"
				>{{e.title}}
					<image class="delete" src="../../static/add.png"></image>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default{
		methods:{
			fanhui(){
				uni.navigateTo({
					url:"/pages/index/main"
				})
			}
		}
	}
</script>

<style>
	.all{
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.top{
		display: flex;
		justify-content: center;
		width: 90vw;
		height: 7vh;
		/* background-color: antiquewhite; */
		font-size: 40rpx;
		border-bottom-style: ridge;
		align-items: center;
	}
	.fanhui{
		position: fixed;
		left: 7vw;
		top:8vh;
		font-size: 50rpx;
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
	.delete{
		position: fixed;
		width: 50rpx;
		height: 50rpx;
	}
</style>