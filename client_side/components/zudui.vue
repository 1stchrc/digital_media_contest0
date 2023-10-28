<template>
	<view class="all">
		<view class="saishi_fenlei">
			<view v-for="(e, i) in queryTags" :key="i">
				<view class="fenlei" v-if="!e.checked" @click="e.checked=true">{{e.text}}</view>
				<view class="fenlei2" v-else @click="e.checked=false">{{e.text}}</view>
			</view>
		</view>
		<view class="detail">
			<view class="detail_left">
				<view class="detailitem" v-for="(e,i) in leftContents" :key="i">
					<view class="user" @click="clickuser()">
						<image class="touxiang" src="/static/logo.png"></image>
						<view class="userid">{{e.leaderName}}</view>
					</view>
					<view class="item_message" @click="clickxiangmu(e.teamId)">{{e.title}}</view>
					<view class="last">
						<image class="shoucang" @click="e.faved=true" v-if="!e.faved" src="/static/shoucang.png"></image>
						<image class="shoucang" v-else src="/static/shoucang_selected.png" @click="e.faved=false"></image>
						<image class="jiejianli" @click="e.liked=true" v-if="!e.liked" src="/static/xihuan.png"></image>
						<image class="jiejianli" v-else src="/static/xihuan_selected.png" @click="e.liked=false"></image>
						<image class="jiejianli" @click=";" v-if="true" src="/static/toujianli.png"></image>
						<image class="jiejianli" v-else src="/static/toujianli.png" @click=";"></image>
					</view>
				</view>
			</view>
			<view class="detail_right">
				<view class="detailitem" v-for="(e,i) in rightContents" :key="i">
					<view class="user" @click="clickuser()">
						<image class="touxiang" src="/static/logo.png"></image>
						<view class="userid">{{e.leaderName}}</view>
					</view>
					<view class="item_message" @click="clickxiangmu(e.teamId)">{{e.title}}</view>
					<view class="last">
						<image class="shoucang" @click="e.faved=true" v-if="!e.faved" src="/static/shoucang.png"></image>
						<image class="shoucang" v-else src="/static/shoucang_selected.png" @click="e.faved=false"></image>
						<image class="jiejianli" @click="e.liked=true" v-if="!e.liked" src="/static/xihuan.png"></image>
						<image class="jiejianli" v-else src="/static/xihuan_selected.png" @click="e.liked=false"></image>
						<image class="jiejianli" @click=";" v-if="true" src="/static/toujianli.png"></image>
						<image class="jiejianli" v-else src="/static/toujianli.png" @click=";"></image>
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
				gd: getApp().globalData,
				queryTags: [
					'理', '工', '农', '医', '文', '史', '哲', '政', '经', '管'
					].map(e=>{return {text: e, checked: false}}),
				leftContents: [],
				rightContents: [],
			}
		},
		async mounted() {
			let res = (await uni.request({
				url: this.gd.serverURL + "/fetch_teams/?team_count=20",
				method: "GET",
			})).data;
			console.log(res);
			for(let i = 0; i < res.length; ++i){
				let el = {
					teamId: res[i].team_id,
					title: res[i].title,
					leaderName: res[i].leader_name,
					faved: false,
					liked: false,
				};
				if(i % 2 === 0)this.leftContents.push(el);
				else this.rightContents.push(el);
			}
		},
		methods: {
			clickxiangmu(id){
				uni.navigateTo({
					url:"/pages/index/zudui_tiezi?id=" + id,
				})
			},
			clickuser(){
				uni.navigateTo({
					url:"/pages/index/mypage"
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
		justify-content: center;
		background-color: rgb(243,243,243);
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
		align-items: center;
		justify-content: center;
		margin-top:2vh;
		width: 100vw;
		margin-left: 5vw;
	}
	.detail_left,.detail_right{
		width: 50vw;
		/* background-color: antiquewhite; */
	}
	.detailitem{
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		width: 40vw;
		/* background-color: aqua; */
		padding: 20rpx;
		box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.15);
		border-radius: 20rpx;
		margin-bottom: 3vh;
		background-color: white;
	}
	.user{
		display: flex;
		align-items: center;
		width: 37vw;
	}
	.touxiang{
		height: 40rpx;
		width: 40rpx;
		border-radius: 50%;
	}
	.userid{
		margin-left: 2vw;
		margin-top: -0.5vh;
	}
	.item_message{
		display: flex;
		justify-content: center;
		align-items: center;
		border-style: solid;
		border-width: 2rpx;
		border-color: rgb(143,143,143);
		border-radius: 20rpx;
		margin-top: 1vh;
		height: 15vh;
		width: 30vw;
	}
	.last{
		display: flex;
		justify-content: space-around;
		width: 32vw;
		margin-top:2vh;
	}
	.shoucang{
		width: 50rpx;
		height: 50rpx;
	}
	.jiejianli{
		margin-left: 4vw;
		width: 50rpx;
		height: 50rpx;
	}
</style>