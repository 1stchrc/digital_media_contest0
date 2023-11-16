<template>
	<view class="all">
		<!-- <view class="fanhui" @click="fanhui()"><</view> -->
		<image class="top" src="../../static/logo.png"></image>
		<view style="margin-top: 1vh; width: 90vw;border-top-style: ridge"></view>
		<view class="each">
			<view class="text">姓名</view>
			<input class="shuru"/>
		</view>
		<view class="each">
			<view class="text">专业</view>
			<input class="shuru"/>
		</view>
		<view class="each">
			<view class="text">年级</view>
			<input class="shuru"/>
		</view>
		<view class="each">
			<view class="text">学历</view>
			<input class="shuru"/>
		</view>
		<view class="zhiweibiaoqian">
			<view class="zhiwei-text">职位标签</view>
			<view class="zhiwei-kuang">
				<view class="zhiwei-each"># 队长</view>
				<view class="zhiwei-each"># 指导教师</view>
				<view class="zhiwei-each"># 运营顾问</view>
				<view class="zhiwei-each"># 文书顾问</view>
				<view class="zhiwei-each"># 技术顾问</view>
				<view class="zhiwei-each"># 美术顾问</view>
			</view>
		</view>
		<view class="biaoqian">
			<view class="biaoqian-text">标签</view>
			<checkbox class="biaoqian-checkbox"></checkbox>
			<input class="biaoqian-input" placeholder="技能描述(与职位对应)"/>
		</view>
		<view class="cansaijingli">
			<view class="cansaijingli-text">参赛经历</view>
			<input class="cansaijingli-input" placeholder="请输入参赛经历"/>
		</view>
	</view>
</template>

<script>
</script>

<style>
	.all{
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.top{
		width: 100rpx;
		height: 100rpx;
		border-radius: 50%;
		margin-top: 2vh;
	}
	.each{
		display: flex;
		justify-content: center;
		margin-top: 2vh;
		width: 66vw;
	}
	.text{
		font-size: 40rpx;
		margin-top: 10rpx;
	}
	.shuru{
		border-style: ridge;
		margin-left: 5vw;
		width: 45vw;
		padding: 10rpx;
	}
	.zhiweibiaoqian{
		width: 80vw;
		height: 20vh;
		/* background-color: aqua; */
		margin-top: 3vh;
	}
	.zhiwei-text{
		font-size: 40rpx;
	}
	.zhiwei-kuang{
		display: flex;
		flex-wrap: wrap;
		justify-content: space-between;
		margin-top: 1vh;
		border-style: ridge;
		height: 15vh;
		padding-left: 4vw;
		padding-right: 4vw;
		padding-top: 1.5vh;
		/* padding-bottom: 0vh; */
		
	}
	.zhiwei-each{
		display: flex;
		align-items: center;
		justify-content: center;
		background-color: #ffffff;
		height: 5vh;
		color: rgb(52,120,246);
		border-radius: 2.5vh;
		box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.35);
		font-size: 30rpx;
		padding-left: 1vw;
		padding-right: 1vw;
		width: fit-content;
	}
	.biaoqian{
		display: flex;
		flex-wrap: wrap;
		width: 80vw;
		height: 18vh;
		margin-top: 5vh;
	}
	.biaoqian-text{
		font-size: 40rpx;
	}
	.biaoqian-checkbox{
		margin-left: 2vw;
	}
	.biaoqian-input{
		margin-top: -5vh;
		width: 80vw;
		height: 3vh;
		padding: 10rpx;
		border-style: ridge;
	}
	.cansaijingli{
		margin-top: -4vh;
		width: 80vw;
	}
	.cansaijingli-text{
		font-size: 40rpx;
	}
	.cansaijingli-input{
		margin-top: 1vh;
		width: 76vw;
		height: 3vh;
		padding: 10rpx;
		border-style: ridge;
	}
</style>