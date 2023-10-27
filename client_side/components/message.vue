<template>
	<view style="background-color: rgb(244,244,244);">
		<view class="message_sort">
			<view v-if="select==0" class="sort_text" style="border-bottom-style: ridge;border-color: rgb(52,120,245);">通知</view>
			<view v-else class="sort_text" @click="clicknotice">通知</view>
			<view class="sort_text" @click="clickliaotian">聊天</view>
			<view v-if="select==2" class="sort_text" style="border-bottom-style: ridge;border-color: rgb(52,120,245);">关注</view>
			<view v-else class="sort_text" @click="clickguanzhu">关注</view>
			</view>
		<view v-if="select==0" class="all">
			<view class="item" v-for="(item,index) in array">
				通知详情
			</view>
		</view>
		<view v-if="select==2" class="all">
			<view class="search-block">
				<view class="search-ico-wapper">
					<image src="/static/search.png" class="search-ico" mode="heightFix"></image>
				</view>
				<input type="text" value="" placeholder="搜索我的关注" class="search-text" maxlength="10" focus/>
			</view>
			<view class="title">
				<view class="title_guanzhu">我的关注({{number}})</view>	
			</view>
			<view class="users">
				<view class="each-user" v-for="(item,index) in array">
					<image class="user-picture" src="/static/logo.png"></image>
					<view class="name-read">
						<view>用户id</view>
						<view class="user-read">{{num[index]}}条内容更新</view>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default{
		data() {
			return {
				number:114514,
				array:["吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码"],
				num:[1,5,3,5,0,6,8,4,2,3,4,9,6,3,6,3,1,2],
				select:0,
				array:["吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码"],
			}
		},
		methods:{
			clicknotice(){
				this.select=0
			},
			clickliaotian(){
				uni.navigateTo({
					url:"/pages/index/chat"
				})
			},
			clickguanzhu(){
				this.select=2
			}
		}
	}
</script>

<style>
	.all{
		display: flex;
		justify-content: center;
		flex-wrap: wrap;
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
		margin-top: 20upx;
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
	.title{
		display: flex;
		margin-top: 3vh;
		margin-left: 0vw;
		width: 90vw;
	}
	.title_guanzhu{
		
	}
	.users{
		height: fit-content;
		margin-top: 2vh;
		width: 95vw;
		overflow-y: auto;
		/* background-color: aliceblue; */
	}
	.each-user{
		display: flex;
		align-items: center;
		height: 15vh;
	}
	.user-picture{
		width: 150rpx;
		height: 150rpx;
		margin-left: 2vw;
		border-radius: 50%;
	}
	.name-read{
		display: flex;
		flex-direction: column;
	}
	.user-read{
		background-color: rgb(244,244,244);
		box-shadow: 0px 0px 5px 0px rgba(0,0,0,0.10);
		margin-top: 1vh;
	}
	/* .all{
		display: flex;
		flex-direction: column;
		background-color: rgb(244,244,244);
		height: fit-content;
		overflow-y: auto;
		align-items: center;
	} */
	.item{
		display: flex;
		background-color: rgb(255,255,255);
		width: 80vw;
		box-shadow: 0px 0px 5px 0px rgba(0, 0, 0, 0.2);
		margin-top:3vh;
		border-radius: 20rpx;
		justify-content: center;
		align-items: center;
		height: 10vh;
	}
	.message_sort{
		display: flex;
		align-items: center;
		/* background-color: aliceblue; */
		width: 100vw;
		height:8vh;
		justify-content: space-around;
		/* margin-left: 5vw; */
		box-shadow: 0px 0px 5px 0px rgba(0, 0, 0, 0.2);
	}
	.sort_text{
		
	}
	.message_item{
		width: 78vw;
		background-color: aliceblue;
		border-style: ridge;
		height: 8vh;
	}
</style>