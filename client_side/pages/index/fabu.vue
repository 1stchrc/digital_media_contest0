<template>
	<view class="all">
		<view class="fanhui" @click="fanhui()"><</view>
		<view class="top">
			发布组队
		</view>
		<input class="bisai-zhaomu" v-model="title" placeholder="**比赛（标题）"></input>
		<view v-for="(e, i) in positions" :key="i" class="zhiwei-jineng-detail">
			<uni-section title="多选" type="line">
				<view class="zhiweibox">
					<!-- <uni-data-checkbox class="zhiwei" multiple v-model="checkbox1" :localdata="hobby"></uni-data-checkbox> -->
					<input class="inputzhiwei" v-model="e.name" placeholder="职位"/>
				</view>
			</uni-section>
			<input class="jineng" v-model="e.desc" placeholder="技能描述"></input>
		</view>
		<view class="add1" @click="positions.push({name:'', desc:''});">
			<image class="add" src="../../static/add.png"></image>
		</view>
		<view class="bottom">
			<image class="cuncaogao" src="../../static/cuncaogao.png" @click="saveDraft()">草稿</image>
			<button class="fabu" @click="confirm()">发布</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				gd : getApp().globalData,
				title: "",
				positions:[{
					name:"",
					desc:""
				}],
			}
		},
		onLoad() {
	
		},
		methods: {
			fanhui(){
				uni.navigateTo({
					url:"/pages/index/main"
				})
			},
			async confirm(){
				await uni.request({
					url: this.gd.serverURL + "/create_team/",
					method: "POST",
					data:{
						user_info : this.gd.userInfo,
						title: this.title,
						positions: this.positions,
					}
				});
				
			}
		}
	}
</script>

<style>
	.fanhui{
		position: fixed;
		left: 7vw;
		top:8vh;
		font-size: 50rpx;
	}
	.all{
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.top{
		display: flex;
		justify-content: center;
		align-items: center;
		/* background-color: beige; */
		width: 90vw;
		height: 8vh;
		border-bottom-style: ridge;
	}
	.bisai-zhaomu{
		display: flex;
		justify-content: center;
		width: 86vw;
		margin-top: 3vh;
		font-size: 50rpx;
		height:6vh;
		border-bottom-style: ridge;
	}
	.jineng{
		
		color: #666;
		font-size: 50rpx;
		margin-left: 9vw;
	}
	.zhiweibox{
		display: flex;
		flex-wrap: nowrap;
	}
	.inputzhiwei{
		position: fixed;
		margin-left: 10vw;
		font-size: 50rpx;
	}
	.zhiwei{
		width: 30vw;
		height: 5vh;
		/* background-color: aliceblue */
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
		border-bottom-style: ridge;
	}
	.add{
		margin-top: 2vh;
		border-radius: 50%;
		margin-left: 3vw;
		width: 65rpx;
		height: 65rpx;
	}
	.add1{
		display: flex;
		width: 90vw;
		height: 10vh;
		/* background-color: antiquewhite; */
	}
	.bottom{
		display: flex;
		align-items: center;
		position: fixed;
		bottom:2vh;
		width: 90vw;
		height: 8vh;
		/* background-color: aliceblue; */
	}
	.cuncaogao{
		margin-left: 2vh;
		margin-right: 1vh;
		width:60rpx;
		height: 60rpx;	
	}
	.fabu{
		margin-left: 15vw;
		display: flex;
		align-items: center;
		justify-content: center;
		width: 50vw;
		height: 5vh;
		border-radius: 50rpx;
		background-color: rgb(52,120,245);
		color:white;
		box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.35);
	}
</style>