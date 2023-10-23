<script>
	export default {
		async onLaunch() {
			console.log('App Launch');
			try{
				this.globalData.userInfo = (await uni.getStorage({
					key : "user_info"
				})).data;
				if(this.globalData.userInfo !== null){
					try{
						await this.globalData.guaranteedLogin(this.globalData.userInfo);
					}catch{
						uni.showToast({
							icon:"error",
							title:"无法连接到服务器",
							duration : 1000,
						})
					}
				}
			}catch{}
		},
		onShow: function() {
			console.log('App Show')
		},
		onHide: function() {
			console.log('App Hide')
		},
		globalData:{
			serverURL : "http://127.0.0.1:8000",
			socketURL : "ws://127.0.0.1:8000",
			userInfo : null,
			webSocketState : "DISCONNECTED",
			async timeout(time){
				return new Promise(res=>{
					setTimeout(res, time);
				});
			},
			guaranteedLogin : async function f(){
				while(this.webSocketState === "DISCONNECTED"){
					try{
						return await this.login(this.userInfo);
						}
					catch{};
				}
			},
			async logout(){
				try{
					await uni.setStorage({
						key : "user_info",
						data : null,
					});
				} catch {
					console.error("无法写入本地存储");
				}
				this.userInfo = null;
				if(this.webSocketState === "DISCONNECTED"){
					return;
				}
				return new Promise(async res=>{
					await uni.onSocketClose(()=>{
						this.webSocketState = "DISCONNECTED";
						console.log("已登出");
						res();
					});
					await uni.closeSocket({
						code: 1000,
					});
				});
			},
			async login(userInfo){
				if(this.webSocketState === "CONNECTED"){
					throw null;
				}
				const heartbeatSender = async ()=>{
					while(this.webSocketState == "CONNECTED"){
						try{
							await uni.onSocketClose(result => {
								console.warn("与服务器断开连接");
								this.webSocketState = "DISCONNECTED";
								this.guaranteedLogin(this.userInfo);
							});
							while(this.webSocketState == "CONNECTED"){
								console.log("发送心跳包...");
								uni.sendSocketMessage({
									data: JSON.stringify({
										type : "HEARTBEAT",
										data : {},
									})
								});
								await this.timeout(150 * 1000);
							}
							return;
						}catch{
							console.warn("发送心跳包出错, 重新发送...");
						}
					}
				}
				console.log("尝试登录...");
				let res = await uni.connectSocket({
					url : this.socketURL + "/login/",
				});
				uni.onSocketError(e => {
					console.warn("登录失败!");
					throw e;
				});
				uni.onSocketOpen(()=>{
					uni.sendSocketMessage({
						data: JSON.stringify({
							type : "BEGIN",
							data : userInfo,
						})
					})
				});
				return new Promise((res, rej)=>{
					uni.onSocketMessage(async msg=>{
						msg = JSON.parse(msg.data);
						switch(msg.type){
							case "BEGIN":{
								console.log("登录成功");
								res(true);
								this.userInfo = userInfo;
								this.webSocketState = "CONNECTED";
								await uni.onSocketMessage(msg=>{});
								heartbeatSender();
								try{
									await uni.setStorage({
										key : "user_info",
										data : userInfo,
									});
								} catch {
									console.error("无法写入本地存储");
								}
								break;
							}
							default:{
								console.log("登录被拒绝!");
								res(false);
								break;
							}
						}
					});
					uni.onSocketClose(msg=>{
						console.warn("登录时断开连接。");
						rej(msg);
					});
				});
			}
		}
	}
</script>

<style>
	/*每个页面公共css */
</style>
