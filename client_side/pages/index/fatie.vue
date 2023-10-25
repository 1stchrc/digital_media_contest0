<template>
	<view class="all">
		<view class="title">发帖子</view>
		<view class="yonghu-biaoti">
			<view class="user">
				<image class="touxiang" src="../../static/logo.png"></image>
				<view class="userid">用户名</view>
			</view>
			<input class="biaoti" placeholder="标题" v-model="draftInfo.title"></input>
		</view>
		<view class="neirong">
			<textarea class="neirong-text" placeholder="内容" v-model="draftInfo.content"></textarea>
		</view>
		<view class="jiaonang">
			<view v-for="(e, i) in draftInfo.tags"
			:key="i">
			<view class="huati-yonghu">{{e}}</view>
			<view style="position: absolute;">
				<view class="tag-delete-confirm">333</view>
			</view>
			</view>
			<input v-if="isAppendingTag" 
			focus="true" class="huati-yonghu" 
			type="text" maxlength="6" 
			placeholder="#话题"
			style="width:16vw;"
			@blur="e=>{if(e.detail.value !== '')draftInfo.tags.push(e.detail.value);isAppendingTag=false;}" >
			</input>
			<image class="add" src="/static/add.png" @click="isAppendingTag=true"></image>
		</view>
		<view class="gongkai_or_simi">
			<image class="simi" src="../../static/simi.png"></image>
			<view class="simi-text">私密</view>
			<switch class="switch" @change="e=>draftInfo.privateFlag=e.detail" :checked="draftInfo.privateFlag" style="transform:scale(0.8);"></switch>
		</view>
		<view class="bottom">
			<image class="cuncaogao" src="../../static/cuncaogao.png" @click="saveDraft()">保存草稿</image>
			<button class="fabu" @click="confirm()">发布</button>
		</view>
	</view>
</template>

<script>
	export default{
		async mounted() {
			this.draftId = this.$route.query.draft_id;
			if(this.draftId !== undefined){
				let draft = (await uni.getStorage({
					key: "posts/drafts/" + this.draftId,
				})).data;
				this.draftInfo = draft;
				this.$forceUpdate();
			}
		},
		data(){
			return{
				gd : getApp().globalData,
				draftId : undefined,
				isAppendingTag : false,
				draftInfo : {
					title : "",
					content : "",
					tags : [],
					privateFlag : false,
				},
			}
		},
		methods:{
			async saveDraft(){
				if(this.draftId === undefined){
					let draftIndices = {top : 0, list : []};
					try{
						draftIndices = (await uni.getStorage({
							key: "posts/draft_indices",
						})).data;
					}catch{}
					this.draftId = draftIndices.top;
					++draftIndices.top;
					draftIndices.list.push(this.draftId);
				}
				let info = {
					title: this.draftInfo.title, 
					content: this.draftInfo.content, 
					tags: this.draftInfo.tags, 
					privateFlag: this.draftInfo.privateFlag,
				};
				await uni.setStorage({
					key : "posts/drafts/" + this.draftId,
					data: info,
				});
				uni.showToast({
					icon: "success",
					title: "草稿已保存",
				})
			},
			async confirm(){
				uni.showLoading({
					title:"发布中...",
				});
				try{
					let res = await uni.request({
						url : this.gd.serverURL + "/post/",
						method : "POST",
						data : {
							user_info:{
								user_id: this.gd.userInfo.user_id,
								password: this.gd.userInfo.password,
							},
							title: this.draftInfo.title,
							content: this.draftInfo.content,
							tags: this.draftInfo.tags,
							private_flag: this.draftInfo.privateFlag,
						},
					});
					if(res.statusCode === 200){
						uni.showToast({
							icon: "success",
							title: "发布成功",
							duration: 1000,
						});
					}else{
						uni.showToast({
							icon: "error",
							title: "请检查登录信息",
							duration: 1000,
						});
					}
				}catch{
					uni.showToast({
						icon:"error",
						title:"与服务器连接失败",
						duration : 1000,
					});
				}
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
	.title{
		display: flex;
		/* background-color: aqua; */
		height: 8vh;
		width: 90vw;
		justify-content: center;
		align-items: center;
		font-size: 35rpx;
		border-bottom-style: ridge;
	}
	.yonghu-biaoti{
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		/* background-color: aquamarine; */
		width: 90vw;
		height: 18vh;
		border-bottom-style: ridge;
	}
	.user{
		display: flex;
		align-items: center;
		height: 9vh;
		margin-left: 2vw;
	}
	.touxiang{
		width: 80rpx;
		height: 80rpx;
		border-radius: 50%;
	}
	.biaoti{
		font-size: 50rpx;
		margin-left: 2vw;
		margin-bottom: 1vh;
	}
	.neirong-text{
		display: flex;
		flex-wrap: wrap;
		width: 85vw;
		height: 30vh;
		margin-top: 1vh;
		margin-bottom: 1vh;
		/* background-color: antiquewhite; */
	}
	.jiaonang{
		display: flex;
		width: 90vw;
		flex-wrap: wrap;
	}
	.huati-yonghu{
		display: flex;
		align-items: center;
		justify-content: center;
		background-color: #ffffff;
		font-size: 50rpx;
		height: 5vh;
		width: fit-content;
		font-family: "黑体";
		color: rgb(52,120,246);
		font-size: 3vh;
		border-radius: 20rpx;
		box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.35);
		margin-left: 3vw;
		overflow: visible;
	}
	.tag-delete-confirm{
		position: inherit;
		bottom: 6vh;
		border: 1rpx;
	}
	.add{
		border-radius: 50%;
		margin-left: 5vw;
		width: 65rpx;
		height: 65rpx;
	}
	.gongkai_or_simi{
		display: flex;
		align-items: center;
		/* background-color: aliceblue; */
		width: 90vw;
		height: 7vh;
		margin-top: 3vh;
		border-top-style: ridge;
		border-bottom-style: ridge;
	}
	.simi{
		margin-left: 2vw;
		width: 50rpx;
		height: 50rpx;
	}
	.simi-text{
		margin-left: 2vw;
	}
	.switch{
		margin-left: 55vw;
	}
	.bottom{
		display: flex;
		align-items: center;
		position: fixed;
		bottom:2vh;
		width: 90vw;
		height: 8vh;
		background-color: aliceblue;
	}
	.cuncaogao{
		margin-left: 2vh;
		margin-right: 1vh;
		width:60rpx;
		height: 60rpx;	
	}
	.fabu{
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