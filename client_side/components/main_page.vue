<template>
	<view class="all">
		<view class="sort_bar">
			<view v-if="selected==0" class="sort_item" style="border-bottom-style: ridge;border-color: rgb(52,120,245);">答疑</view>
			<view v-else class="sort_item" @click="clickdayi()">答疑</view>
			<view v-if="selected==1" class="sort_item" style="border-bottom-style: ridge;border-color: rgb(52,120,245);">经验分享</view>
			<view v-else class="sort_item" @click="clickjingyanfenxiang()">经验分享</view>
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
				<view v-for="(e, i) in leftContents"
				:key="i"
				class="detail_left_item" @click="open_detail"
				>{{e.title}}</view>
			</view>
			<view class="detail_right">
				<view v-for="(e, i) in rightContents"
				:key="i"
				class="detail_right_item" @click="open_detail"
				>{{e.title}}</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default{
		mounted() {
			this.getContent();
		},
		data(){
			return {
				gd: getApp().globalData,
				leftContents: [],
				rightContents: [],
				selected:0
			}
		},
		methods:{
			async getContent(){
				try{
					let ret = await uni.request({
						url: this.gd.serverURL + "/fetch_posts/?post_count=10",
						method: "GET",
					});
					if(ret.statusCode !== 200){
						console.error("wtf");
						return;
					}
					for(let i = 0; i < ret.data.length; ++i){
						if(i % 2){
							this.leftContents.push(ret.data[i]);
						}else{
							this.rightContents.push(ret.data[i]);
						}
					}
				}catch{}
			},
			open_detail(){
				uni.navigateTo({
					url:"/pages/index/tiezi_detail"
				})
			},
			clickdayi(){
				this.selected=0
			},
			clickjingyanfenxiang(){
				this.selected=1
			}
		}
	}
</script>

<style>
	.sort_bar{
		display: flex;
		align-items: center;
		justify-content: space-around;
		width: 100vw;
		height: 7vh;
		/* border-bottom-style: solid; */
		box-shadow: 0px 0px 5px 0px rgba(0, 0, 0, 0.2);
		margin-bottom: 1vh;
		
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