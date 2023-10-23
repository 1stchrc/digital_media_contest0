<template>
	<view class="all">
		<view class="saishi_fenlei">
			<view class="fenlei">理</view>
			<view class="fenlei">工</view>
			<view class="fenlei">农</view>
			<view class="fenlei">医</view>
			<view class="fenlei">文</view>
			<view class="fenlei">史</view>
			<view class="fenlei">哲</view>
			<view class="fenlei">政</view>
			<view class="fenlei">经</view>
			<view class="fenlei">管</view>
		</view>
		<view class="detail">
			<view class="detail_left">
				<view class="detailitem" v-for="(item,index) in array">
					<view class="user">
						<image class="touxiang" src="/static/logo.png"></image>
						<view class="userid">用户名</view>
					</view>
					<view class="item_message">{{item}}</view>
					<view class="last">
						<image class="shoucang" @click="clickshoucang_left(index)" v-if="shoucang_left[index]==0" src="/static/shoucang.png"></image>
						<image class="shoucang" v-else src="/static/shoucang_selected.png" @click="clickshoucang_left(index)"></image>
						<image class="jiejianli" @click="clickxihuan_left(index)" v-if="xihuan_left[index]==0" src="/static/xihuan.png"></image>
						<image class="jiejianli" v-else src="/static/xihuan_selected.png" @click="clickxihuan_left(index)"></image>
					</view>
				</view>
			</view>
			<view class="detail_right">
				<view class="detailitem" v-for="(item,index) in array">
					<view class="user">
						<image class="touxiang" src="/static/logo.png"></image>
						<view class="userid">用户名</view>
					</view>
					<view class="item_message">{{item}}</view>
					<view class="last">
						<image class="shoucang" @click="clickshoucang_right(index)" v-if="shoucang_right[index]==0" src="/static/shoucang.png"></image>
						<image class="shoucang" v-else src="/static/shoucang_selected.png" @click="clickshoucang_right(index)"></image>
						<image class="jiejianli" @click="clickxihuan_right(index)" v-if="xihuan_right[index]==0" src="/static/xihuan.png"></image>
						<image class="jiejianli" v-else src="/static/xihuan_selected.png" @click="clickxihuan_right(index)"></image>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				array:["吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码"],
				shoucang_left:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				xihuan_left:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				shoucang_right:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
				xihuan_right:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			}
		},
		onLoad() {
	
		},
		methods: {
			clickshoucang_left(x){
				this.shoucang_left[x]=!this.shoucang_left[x];
				this.$forceUpdate();
			},
			clickxihuan_left(x){
				this.xihuan_left[x]=!this.xihuan_left[x];
				this.$forceUpdate();
			},
			clickshoucang_right(x){
				this.shoucang_right[x]=!this.shoucang_right[x];
				this.$forceUpdate();
			},
			clickxihuan_right(x){
				this.xihuan_right[x]=!this.xihuan_right[x];
				this.$forceUpdate();
			},
			
		}
	}
</script>

<style>
	.all{
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	.saishi_fenlei{
			display: flex;
			align-items: center;
			flex-wrap:wrap;
			justify-content: space-around;
			padding:10rpx;
			margin-top:2vw;
			height: 15vh;
			width: 95vw;
			background-color: white;
			border-radius: 20rpx;
			/* box-shadow: 0px 0px 50px 0px rgba(0,0,0,0.15); */
		}
		.fenlei{
			display: flex;
			align-items: center;
			justify-content: center;
			background-color: #ffffff;
			font-size: 50rpx;
			height: 5vh;
			width:16vw;
			font-family: "黑体";
			color: rgb(52,120,246);
			font-size: 3vh;
			border-radius: 2.5vh;
	/* 		border-style: solid;
			border-color: grey;
			border-width: 1rpx; */
			box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.35);
		}
	
	.detail{
		display: flex;
		margin-top:2vh;
	}
	.detail_left{
		justify-content: space-around;
		width: 50vw;
		background-color: antiquewhite;
	}
	.detail_right{
		justify-content: space-around;
		width: 50vw;
		background-color: antiquewhite;
	}
	.detailitem{
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		margin-top: 1vh;
		margin-left: 3vh;
		width: 36vw;
		background-color: aqua;
		padding: 20rpx;
	}
	.user{
		display: flex;
	}
	.touxiang{
		height: 60rpx;
		width: 60rpx;
	}
	.userid{
		margin-left: 3vw;
	}
	.item_message{
		margin-left: 3vw;
	}
	.last{
		margin-top:3vh;
	}
	.shoucang{
		width: 60rpx;
		height: 60rpx;
	}
	.jiejianli{
		margin-left: 4vw;
		width: 60rpx;
		height: 60rpx;
	}
</style>