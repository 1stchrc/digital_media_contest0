<script>
	export default {
		async onLaunch() {
			console.log('App Launch');
			try{
				this.globalData.userInfo = (await uni.getStorage({
					key : "user_info"
				})).data;
				try{
					await this.globalData.guaranteedLogin(this.globalData.userInfo);
				}catch{
					uni.showToast({
						icon:"error",
						title:"无法连接到服务器",
						duration : 1000,
					})
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
					catch{};
				}
			},
			async login(userInfo){
				if(this.webSocketState === "CONNECTED"){
					throw null;
				}
				const that = this;
				const heartbeatSender = async function f(){
					try{
						try{
							await uni.onSocketClose(result => {
								console.warn("与服务器断开连接");
								that.webSocketState = "DISCONNECTED";
								that.guaranteedLogin(that.userInfo);
							});
						}catch(e){
							console.log("?");
							throw e;
						}
						while(that.webSocketState == "CONNECTED"){
							console.log("发送心跳包...");
							uni.sendSocketMessage({
								data: JSON.stringify({
									type : "HEARTBEAT",
									data : {},
								})
							});
							await that.timeout(150 * 1000);
						}
					}catch{
						console.warn("发送心跳包出错, 重新发送...");
						return await f();
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
								res(false);
								break;
							}
						}
					});
					uni.onSocketClose(msg=>{
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
