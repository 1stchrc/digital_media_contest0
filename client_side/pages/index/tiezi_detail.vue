<template>
	<view class="all">
		<view class="user">
			<image class="touxiang" src="../../static/logo.png"></image>
			<view class="userid">用户名</view>
			<view class="user_guanzhu" v-if="guanzhu==0" @click="guanzhu1()">关注</view>
			<view class="user_guanzhu" v-else @click="guanzhu1()">已关注</view>
		</view>
		<view class="zhengwen">
			<view class="title">
				这里是题目
			</view>
			<view class="detail">
				这里是正文这里是正文这里是正文这里是正文这里是正文这里是正文这里是正文这里是正文这里是正文这里是正文这里是正文这里是正文这里是正文这里是正文这里是正文这里是正文这里是正文这里是正文这里是正文这里是正文这里是正文这里是正文这里是正文这里是正文
			</view>
			<image class="image" src="../../static/add.png"></image>
		</view>
		<view class="bottom">
			<input class="pinglun" placeholder="评论"></input>
			<image class="dianzan" v-if="dianzan==0" @click="dianzan1()" src="../../static/xihuan.png"></image>
			<image class="dianzan" v-else @click="dianzan1()" src="../../static/xihuan_selected.png"></image>
			<image class="shoucang" v-if="shoucang==0" @click="shoucang1()" src="../../static/shoucang.png"></image>
			<image class="shoucang" v-else @click="shoucang1()" src="../../static/shoucang_selected.png"></image>
		</view>
	</view>
</template>

<script>
	export default{
		data(){
			return{
				guanzhu:false,
				dianzan:false,
				shoucang:false
			}
		},
		methods:{
			guanzhu1(){
				this.guanzhu=!this.guanzhu
			},
			dianzan1(){
				this.dianzan=!this.dianzan
			},
			shoucang1(){
				this.shoucang=!this.shoucang
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
	.user{
		position: fixed;
		background-color: white;
		display: flex;
		align-items: center;
		width: 90vw;
		height: 9vh;
		border-bottom-style: ridge;
	}
	.touxiang{
		width: 80rpx;
		height: 80rpx;
		border-radius: 50%;
		margin-left: 2vw;
	}
	.user_guanzhu{
		display: flex;
		align-items: center;
		justify-content: center;
		margin-left: 24vh;
		border-style: ridge;
		border-radius: 20rpx;
		width: 18vw;
		height: 4.5vh;
	}
	.zhengwen{
		margin-top: 9vh;
		width: 90vw;
		padding-bottom: 3vh;
		overflow-y: auto;
		/* background-color: aquamarine; */
	}
	.title{
		/* background-color: aqua; */
		margin-top: 3vh;
		margin-left: 1vw;
		width: 89vw;
		height: 5vh;
		font-size: 50rpx;
	}
	.detail{
		margin-top: 5vh;
		margin-left: 1vw;
		margin-right: 1vw;
	}
	.image{
		width: 90vw;
		margin-top: 1vh;
		margin-bottom: 1vh;
	}
	.bottom{
		display: flex;
		align-items: center;
		position: fixed;
		bottom: 0;
		width: 90vw;
		height: 7vh;
		background-color: white;
		border-top-style: ridge;
	}
	.pinglun{
		width: 60vw;
		border-style: ridge;
		border-radius: 30rpx;
		border-color: rgb(243,243,243);
		padding-left: 3vw;
		
	}
	.dianzan,.shoucang{
		width: 50rpx;
		height: 50rpx;
	}
	.dianzan{
		margin-left: 5vw;
	}
	.shoucang{
		margin-left: 4vw;
		margin-bottom: 0.3vh;
	}
</style>