<template>
	<view>
		<swiper class="swiper" @change="e=>selected_page = e.detail.current" :current="selected_page">
			<swiper-item>
				<main-page></main-page>
				<view style="height: 10vh;" />
			</swiper-item>
			<swiper-item>
				<message></message>
				<view style="height: 10vh;" />
			</swiper-item>
			<swiper-item>
				<zudui></zudui>
				<view style="height: 10vh;" />
			</swiper-item>
			<swiper-item>
				<mypage></mypage>
				<view style="height: 10vh;" />
			</swiper-item>
		</swiper>
		
		<view class="tabbar">
			<view class="tabbar_item">
				<image class="tabbar_item_image" v-if="selected_page!=0"src="../../static/homepage.png" @click="selected_page = 0"></image>
				<image class="tabbar_item_image" v-else src="../../static/homepage_selected.png"></image>
				<view class="tabbar_text" v-if="selected_page!=0" @click="selected_page = 0">首页</view>
				<view class="tabbar_text_selected" v-else>首页</view>
			</view>
			<view class="tabbar_item">
				<image class="tabbar_item_image" v-if="selected_page!=1"src="../../static/message.png" @click="selected_page = 1"></image>
				<image class="tabbar_item_image" v-else src="../../static/message_selected.png"></image>
				<view class="tabbar_text" v-if="selected_page!=1" @click="selected_page = 1">消息</view>
				<view class="tabbar_text_selected" v-else>消息</view>
			</view>
			<image class="tabbar_image" @click="fabu" src='/static/add.png'></image>
			<view class="tabbar_item">
				<image class="tabbar_item_image" v-if="selected_page!=2"src="../../static/zudui.png" @click="selected_page = 2"></image>
				<image class="tabbar_item_image" v-else src="../../static/zudui_choose.png"></image>
			<view class="tabbar_text" v-if="selected_page!=2" @click="selected_page = 2">组队</view>
			<view class="tabbar_text_selected" v-else>组队</view>
			</view>
			<view class="tabbar_item">
				<image class="tabbar_item_image" v-if="selected_page!=3"src="../../static/mypage.png" @click="selected_page = 3"></image>
				<image class="tabbar_item_image" v-else src="../../static/mypage_selected.png"></image>
			<view class="tabbar_text" v-if="selected_page!=3" @click="selected_page = 3">我的</view>
			<view class="tabbar_text_selected" v-else>我的</view>
			</view>
		</view>
		<view class="tabbox" v-if="tabbox1==1" @click="fabu()">
			<view class="jiemian">
				<view class="each-item" @click="clickfabu()">
					发布
				</view>
				<view class="each-item" @click="clickcaogao()">
					草稿
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	import main_page from "@/components/main_page.vue";
	import message from "@/components/message.vue";
	import zudui from "@/components/zudui.vue";
	import mypage from "@/components/mypage.vue";
	export default{
		data(){
			return{
				selected_page : 0,
				tabbox1:0
			};
		},
		components:{
			"main-page":main_page,
			"message":message,
			"zudui":zudui,
			"mypage":mypage,
		},
		methods:{
			fabu(){
				this.tabbox1=!this.tabbox1
			},
			clickfabu(){
				uni.navigateTo({
					url:"/pages/index/fabu"
				})
			},
			clickcaogao(){
				uni.navigateTo({
					url:"/pages/index/draft_box"
				})
			}
		}
	}
</script>

<style>
	.tabbox{
		display: flex;
		justify-content: center;
		position: fixed;
		background-color: rgba(149, 149, 149, 0.5);
		width: 100vw;
		height: 100vh;
		top:0;
		left:0;
	}
	.jiemian{
		position: fixed;
		background-color: white;
		width: 20vw;
		height: 15vh;
		bottom: 10vh;
		border-radius: 20rpx;
	}
	.each-item{
		display: flex;
		justify-content: center;
		align-items: center;
		/* background-color: aqua; */
		width: 20vw;
		height: 7.5vh;
		font-size: 40rpx;
	}
	.swiper{
		height: 90vh;
	}
	.swiper swiper-item{
		overflow-x: hidden;
		overflow-y: scroll;
	}
	.tabbar{
		display: flex;
		align-items: center;
		justify-content: space-around;
		position: fixed;
		bottom: 0;
		background-color: #ffffff;
		box-shadow: 0 -1px 3px rgba(0, 0, 0, 0.1);
		height: 10vh;
		width: 100vw;
	}
	.tabbar_item{
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.tabbar_item_image{
		width:50rpx;
		height:50rpx;
	}
	.tabbar_image{
		height: 100rpx;
		width: 100rpx;
		
	}
	
	.tabbar_text, .tabbar_text_selected{
		font-family: "黑体";
		font-size: 3vh;
	}
	.tabbar_text_selected{
		color:rgb(52,120,246);
	}
</style>