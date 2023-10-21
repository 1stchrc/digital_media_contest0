<template>
	<view>
		<view class="name">
			姓名
		</view>
		<view class="sex_tele">
			<view class="sex">
				性别
			</view>
			<view class="tele">
				联系方式
			</view>
		</view>
		<view class="xueli_zhuanye">
			<view class="xueli">
				学历
			</view>
			<view class="zhuanye">
				专业
			</view>
		</view>
		<view class="cansaijingli">
			参赛经历/项目经历
		</view>
		<view class="cansaijingli_detail">
			???
		</view>
		<view class="identify">
			证明
		</view>
		<view class="role">
			职位/角色
		</view>
		<image class="add" src="../../static/zhuye_jiahao.png"></image>
	</view>
</template>

<script>
</script>

<style>
	.name{
		margin-top: 5vh;
		margin-left: 10vw;
	}
	.sex_tele{
		display: flex;
	}
	.sex{
		margin-top: 5vh;
		margin-left: 10vw;
	}
	.tele{
		margin-top: 5vh;
		margin-left: 10vw;
	}
	.xueli_zhuanye{
		display: flex;
	}
	.xueli{
		margin-top: 5vh;
		margin-left: 10vw;
	}
	.zhuanye{
		margin-top: 5vh;
		margin-left: 10vw;
	}
	.cansaijingli{
		margin-top: 5vh;
		margin-left: 10vw;
	}
	.cansaijingli_detail{
		margin-top: 2vh;
		margin-left: 10vw;
		border-style: ridge;
		width: 80vw;
		height: 5vh;
	}
	.identify{
		margin-top: 2vh;
		margin-left: 20vw;
		border-style: ridge;
		width: 70vw;
		height: 5vh;
	}
	.role{
		margin-top: 2vh;
		margin-left: 20vw;
		border-style: ridge;
		width: 70vw;
		height: 5vh;
	}
	.add{
		position: fixed;
		width: 80rpx;
		height: 80rpx;
		top:49vh;
		left:8vw;
	}
</style>