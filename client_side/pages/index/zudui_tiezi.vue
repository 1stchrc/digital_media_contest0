<template>
	<view class="all">
		<view class="user">
			<image class="touxiang" src="../../static/logo.png"></image>
			<view class="userid">{{teamInfo.leader_info.name}}</view>
			<view class="user_guanzhu" v-if="guanzhu==0" @click="guanzhu1()">关注</view>
			<view class="user_guanzhu" v-else @click="guanzhu1()">已关注</view>
		</view>
		<view class="bisai-zhaomu">
			{{teamInfo.title}}
		</view>
		<view class="zhiwei-jinengmiaoshu">
			<view v-for="(e, i) in teamInfo.positions" :key="i" class="zhiwei-jineng-detail">
				<!-- <uni-section title="多选" type="line">
					<view class="uni-px-5 uni-pb-5">
						<uni-data-checkbox class="zhiwei" multiple v-model="checkbox1" :localdata="hobby"></uni-data-checkbox>
					</view>
				</uni-section> -->
				<view class="jineng">{{e.name}}</view>
				<view class="jineng">{{e.desc}}</view>
			</view>
		</view>
		<view class="bottom">
			<image class="dianzan" v-if="dianzan==0" @click="dianzan1()" src="../../static/xihuan.png"></image>
			<image class="dianzan" v-else @click="dianzan1()" src="../../static/xihuan_selected.png"></image>
			<image class="shoucang" v-if="shoucang==0" @click="shoucang1()" src="../../static/shoucang.png"></image>
			<image class="shoucang" v-else @click="shoucang1()" src="../../static/shoucang_selected.png"></image>
			<view class="toudi">投递简历</view>
		</view>
	</view>
</template>

<script>
	export default{
		data(){
			return{
				gd: getApp().globalData,
				teamId: this.$route.query.id,
				teamInfo: {title:"", positions:"", leader_info:{name:""}},
				guanzhu:false,
				dianzan:false,
				shoucang:false,
			}
		},
		async onLoad(){
			this.teamInfo = (await uni.request({
				url:this.gd.serverURL + "/team_detail/?team_id="+this.teamId,
			})).data;
			this.$forceUpdate();
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
	.jineng{
		
		color: #666;
		font-size: 25px;
		margin-left: 9vw;
	}
	.zhiwei{
		width: 30vw;
		height: 5vh;
		/* background-color: aliceblue */
	}
	.bisai-zhaomu{
		display: flex;
		flex-direction: column;
		align-items: center;
		/* background-color: aqua; */
		width: 90vw;
		height: 6vh;
		font-size: 50rpx;
		margin-top: 12vh;
	}
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
		border-style: solid;
		border-color: aliceblue;
		border-radius: 20rpx;
		width: 18vw;
		height: 4.5vh;
		box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.35);
	}
	.bottom{
		display: flex;
		align-items: center;
		position: fixed;
		bottom: 0;
		width: 90vw;
		height: 8vh;
		background-color: white;
		border-top-style: ridge;
	}
	.dianzan,.shoucang{
		width: 50rpx;
		height: 50rpx;
	}
	.dianzan{
		margin-left: 3vw;
	}
	.shoucang{
		margin-left: 5vw;
		margin-bottom: 0.3vh;
	}
	.toudi{
		display: flex;
		justify-content: center;
		align-items: center;
		color: white;
		margin-left: 15vw;
		border-radius: 30rpx;
		background-color: rgb(52,120,245);
		width: 50vw;
		height: 5vh;
		box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.35);
		
	}
	.zhiwei-jinengmiaoshu{
		display: flex;
		flex-direction: column;
		justify-content: space-around;
		align-items: center;
		/* background-color: aqua; */
		width: 90vw;
		height: 50vh;
	}
	.zhiwei-jineng-detail{
		display: flex;
		flex-direction: column;
		justify-content: space-around;
		/* background-color: antiquewhite; */
		width: 88vw;
		height: 20vh;
		
	}
</style>