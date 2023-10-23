<template>
	<view class="all">
		<view class="saishi_fenlei">
			<view class="fenlei" v-if="li_clicked==0" @click="clickli">理</view>
			<view class="fenlei2" v-else @click="clickli">理</view>
			<view class="fenlei" v-if="gong_clicked==0" @click="clickgong">工</view>
			<view class="fenlei2" v-else @click="clickgong">工</view>
			<view class="fenlei" v-if="nong_clicked==0" @click="clicknong">农</view>
			<view class="fenlei2" v-else @click="clicknong">农</view>
			<view class="fenlei" v-if="yi_clicked==0" @click="clickyi">医</view>
			<view class="fenlei2" v-else @click="clickyi">医</view>
			<view class="fenlei" v-if="wen_clicked==0" @click="clickwen">文</view>
			<view class="fenlei2" v-else @click="clickwen">文</view>
			<view class="fenlei" v-if="shi_clicked==0" @click="clickshi">史</view>
			<view class="fenlei2" v-else @click="clickshi">史</view>
			<view class="fenlei" v-if="zhe_clicked==0" @click="clickzhe">哲</view>
			<view class="fenlei2" v-else @click="clickzhe">哲</view>
			<view class="fenlei" v-if="zheng_clicked==0" @click="clickzheng">政</view>
			<view class="fenlei2" v-else @click="clickzheng">政</view>
			<view class="fenlei" v-if="jing_clicked==0" @click="clickjing">经</view>
			<view class="fenlei2" v-else @click="clickjing">经</view>
			<view class="fenlei" v-if="guan_clicked==0" @click="clickguan">管</view>
			<view class="fenlei2" v-else @click="clickguan">管</view>
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
				li_clicked:0,
				gong_clicked:0,
				nong_clicked:0,
				yi_clicked:0,
				wen_clicked:0,
				shi_clicked:0,
				zhe_clicked:0,
				zheng_clicked:0,
				jing_clicked:0,
				guan_clicked:0
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
			clickli(){
				this.li_clicked=!this.li_clicked
			},
			clickgong(){
				this.gong_clicked=!this.gong_clicked
			},
			clicknong(){
				this.nong_clicked=!this.nong_clicked
			},
			clickyi(){
				this.yi_clicked=!this.yi_clicked
			},
			clickwen(){
				this.wen_clicked=!this.wen_clicked
			},
			clickshi(){
				this.shi_clicked=!this.shi_clicked
			},
			clickzhe(){
				this.zhe_clicked=!this.zhe_clicked
			},
			clickzheng(){
				this.zheng_clicked=!this.zheng_clicked
			},
			clickjing(){
				this.jing_clicked=!this.jing_clicked
			},
			clickguan(){
				this.guan_clicked=!this.guan_clicked
			}
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
		box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.35);
	}
	.fenlei2{
		display: flex;
		align-items: center;
		justify-content: center;
		background-color: rgb(52,120,246);
		font-size: 50rpx;
		height: 5vh;
		width:16vw;
		font-family: "黑体";
		color: #ffffff;
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