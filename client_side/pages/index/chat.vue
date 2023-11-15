<template>
	<view class="chat-all">
		<view class="left">
			<image class="user-picture" src="/static/logo.png"></image>
			<view class="chat-duixiang">
				<image class="duixiang-image" src="/static/logo.png"></image>
				<image class="duixiang-image" src="/static/logo.png"></image>
				<image class="duixiang-image" src="/static/logo.png"></image>
				<image class="duixiang-image" src="/static/logo.png"></image>
				<image class="duixiang-image" src="/static/logo.png"></image>
			</view>
		</view>
		<view class="right">
			<view class="richeng-tixing" @click="routineExpanded = !routineExpanded">
				<image class="daosanjiao" src="/static/daosanjiao.png" v-if="routineExpanded"></image>
				<image v-else class="yousanjiao" src="/static/daosanjiao.png"></image>
				日程提醒
			</view>
			<view class="tixing-detail" v-if="routineExpanded">
				<image class="richeng-image" src="/static/richeng.png"></image>
				<view class="richeng-text">***</view>
				<view class="richeng-jindu">
					完成度90%
				</view>
			</view>
			<view class="xiaoxi" @click="chatExpanded = !chatExpanded">
				<image class="daosanjiao" src="/static/daosanjiao.png" v-if="chatExpanded"></image>
				<image class="yousanjiao" src="/static/daosanjiao.png" v-else></image>
				消息
			</view>
			<view v-if="chatExpanded">
				<view v-if="ismore==0" class="chat-box">
					<view v-for="el, idx in chats" :key="idx" class="chat-content-wrap">
						<view v-if="el.ownedBySelf" class="chat-content-self">
							<view class="peer-title">
								{{el.title}}
							</view>
							<view class="chat-child-wrap">
								<view class="chat-content">
									{{el.content}}
								</view>
								<image class="duixiang-image" src="/static/logo.png"></image>
							</view>
						</view>
						<view v-else class="chat-content-other">
							<view class="peer-title">
								{{el.title}}
							</view>
							<view class="chat-child-wrap">
								<image class="duixiang-image" src="/static/logo.png"></image>
								<view class="chat-content">
									{{el.content}}
								</view>
							</view>
						</view>
					</view>
				</view>
				<view v-else class="chat-box chat-box-detail">
					<view v-for="el, idx in chats" :key="idx" class="chat-content-wrap">
						<view v-if="el.ownedBySelf" class="chat-content-self">
							<view class="peer-title">
								{{el.title}}
							</view>
							<view class="chat-child-wrap">
								<view class="chat-content">
									{{el.content}}
								</view>
								<image class="duixiang-image" src="/static/logo.png"></image>
							</view>
						</view>
						<view v-else class="chat-content-other">
							<view class="peer-title">
								{{el.title}}
							</view>
							<view class="chat-child-wrap">
								<image class="duixiang-image" src="/static/logo.png"></image>
								<view class="chat-content">
									{{el.content}}
								</view>
							</view>
						</view>
					</view>
				</view>
			</view>
			<view class="chat-shuru">
				<input @confirm="chatConfirmEvent" v-model="chatInputText" class="chat-shurukuang" placeholder="请输入发送内容"/>
				<image class="chat-more" src="/static/add.png" @click="clickmore()"></image>
			</view>
			<view class="more-detail" v-if="ismore==1">
				<image class="more-item" src="/static/tupian.png"></image>
				<image class="more-item" src="/static/wenjian.png"></image>
				<image class="more-item" src="/static/shipin.png"></image>
			</view>
		</view>
	</view>
</template>

<script>
	export default{
		data(){
			return{
				routineExpanded : true,
				chatExpanded : true,
				ismore: 0,
				chatInputText : "",
				chats:[
					{
						ownedBySelf : false,
						title : "fff",
						content : "abcdefg",
					},
					{
						ownedBySelf : false,
						title : "aaabbb",
						content : "asdasd\nasdasd\nasd",
					},
					{
						ownedBySelf : true,
						title : "ok",
						content : "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
					},
				],
			}
		},
		methods:{
			clickmore(){
				this.ismore=!this.ismore
			},
			chatConfirmEvent(e){
				this.chats.push({
					ownedBySelf : true,
					title : "ok",
					content : e.detail.value,
				});
				this.chatInputText = "";
				this.$forceUpdate();
			},
		}
	}
</script>

<style>
	.chat-all{
		display: flex;
	}
	.left{
		display: flex;
		flex-direction: column;
		align-items: center;
		width: 17vw;
		height: 100vh;
		border-right-style: ridge;
		/* background-color: antiquewhite; */
	}
	.user-picture{
		border-radius: 50%;
		margin-top: 2vh;
		width: 120rpx;
		height: 120rpx;
	}
	.chat-duixiang{
		display: flex;
		flex-direction: column;
		align-items: center;
		border-top-style: ridge;
		margin-top: 1vh;
		width: 18vw;
	}
	.duixiang-image{
		width: 120rpx;
		height: 120rpx;
		margin-top: 1vh;
	}
	.right{
		display: flex;
		flex-direction: column;
		align-items: center;
		/* justify-content: center; */
		width: 83vw;
		height: 100vh;
		/* background-color: cadetblue; */
	}
	.richeng-tixing{
		display: flex;
		align-items: center;
		width: 83vw;
		height: 8vh;
		/* background-color: aliceblue; */
		font-size: 35rpx;
	}
	.daosanjiao{
		width: 30rpx;
		height: 30rpx;
		margin-left: 5vw;
		margin-right: 2vw;
		margin-top: 0.5vh;
	}
	.yousanjiao{
		width: 30rpx;
		height: 30rpx;
		margin-left: 5vw;
		margin-right: 2vw;
		margin-top: 0.5vh;
		transform: rotate(-90deg);
	}
	.tixing-detail{
		display: flex;
		align-items: center;
		border-style: solid;
		border-radius: 20rpx;
		width: 65vw;
		height: 7vh;
		border-width: 2rpx;
		border-color: rgb(143,143,143);
		
	}
	.richeng-image{
		width: 50rpx;
		height: 50rpx;
		margin-left: 2vw;
		margin-right: 2vw;
	}
	.richeng-text{
		width: 30vw;
		/* font-size: 30rpx; */
	}
	.richeng-jindu{
		font-size: 30rpx;
		color: rgb(143,143,143);
	}
	.xiaoxi{
		width: 83vw;
		margin-top: 3vh;
	}
	.chat-box{
		width: 65vw;
		height: 62vh;
		border-style: solid;
		border-width: 2rpx;
		border-color: rgb(143,143,143);
		margin-top: 3vh;
		margin-bottom: 3vh;
		border-radius: 20rpx;
		overflow-y: scroll;
	}
	.chat-box-detail{
		height: 48vh;
	}
	.chat-shuru{
		display: flex;
		justify-content: space-around;
		align-items: center;
		width: 65vw;
		height: 6vh;
		/* border-style: solid; */
		margin-top: 1vh;
		/* border-radius: 20rpx; */
	}
	.chat-shurukuang{
		border-style: solid;
		border-width: 2rpx;
		border-color: rgb(143,143,143);
		border-radius: 20rpx;
		width: 53vw;
		height: 6vh;
	}
	.chat-more{
		width: 70rpx;
		height: 70rpx;
		border-radius: 50%;
		margin-left: 2vw;
	}
	.more-detail{
		display: flex;
		flex-wrap: wrap;
		justify-content: space-around;
		align-items: center;
		margin-top: 3vh;
		width: 66vw;
		height: 13vh;
		border-style: solid;
		border-radius: 20rpx;
		border-width: 2rpx;
		border-color: rgb(143,143,143);
		/* box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.35); */
		/* background-color: rgb(238, 238, 238); */
	}
	.more-item{
		width: 90rpx;
		height: 90rpx;
		/* border-style: solid;
		border-width: 2rpx;
		border-color: rgb(143,143,143); */
	}
	.chat-content-wrap{
		width: 100%;
	}
	.chat-content-self{
		display: flex;
		flex-direction: column;
		align-items: flex-end;
	}
	.chat-content-other{
		display: flex;
		flex-direction: column;
		align-items: flex-start;
	}
	.chat-content{
		margin-top: 20rpx;
		white-space: pre-line;
		word-break: break-all;
		border-width: 3rpx;
		border-style: solid;
		border-radius: 3vw;
		width: fit-content;
		max-width: 65%;
		height: fit-content;
		padding: 12rpx;
	}
	.chat-content-self .chat-child-wrap{
		display: flex;
		justify-content: flex-end;
	}
	.chat-content-other .chat-child-wrap{
		display: flex;
		justify-content: flex-end;
	}
	.peer-title{
		width: fit-content;
		height: 1rem;
		margin-top: 0rpx;
		margin-left: 20rpx;
		margin-right: 20rpx;
		margin-bottom: -10rpx;
	}
</style>