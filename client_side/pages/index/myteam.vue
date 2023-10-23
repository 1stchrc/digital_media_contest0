<template>
	<view>
		<view class="all">
			<view class="search-block">
				<view class="search-ico-wapper">
					<image src="/static/search.png" class="search-ico" mode="heightFix"></image>
				</view>
				<input type="text" value="" placeholder="搜索我的团队" class="search-text" maxlength="10" focus/>
			</view>
		</view>
		<view class="title">
			<view class="title_guanzhu">我的团队({{number}})</view>	
		</view>
		<view class="users">
			<view class="each-user" v-for="(item,index) in array">
				<image class="user-picture" src="../../static/logo.png"></image>
				<view class="name-read">
					<view>{{item}}</view>
					<view class="user-read">{{num[index]}}条消息未读</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default{
		data(){
			return {
				number:114514,
				array:["吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码","吃饭","睡觉","打代码"],
				num:[1,5,3,5,0,6,8,4,2,3,4,9,6,3,6,3,1,2]
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
		margin-top: 5vh;
		margin-left: 5vw;
	}
	.title_guanzhu{
		
	}
	.users{
		height: fit-content;
		margin-top: 3vh;
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
</style>