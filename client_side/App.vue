<script>
	export default {
		onLaunch: function() {
			console.log('App Launch')
		},
		onShow: function() {
			console.log('App Show')
		},
		onHide: function() {
			console.log('App Hide')
		},
		globalData:{
			userId : null,
			serverURL : "http://127.0.0.1:8000",
			navigateTo : (obj)=>{
				return new Promise((resolve, reject)=>{
					obj.success = resolve;
					obj.fail = reject;
					uni.navigateTo(obj);
				});
			},
			request : (obj)=>{
				return new Promise((resolve, reject)=>{
					obj.success = resolve;
					obj.fail = reject;
					uni.request(obj);
				})
			},
			timeout : (time)=>{
				return new Promise(res=>{
					setTimeout(res, time);
				});
			}
		}
	}
</script>

<style>
	/*每个页面公共css */
</style>
