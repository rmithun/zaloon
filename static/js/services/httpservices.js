//URL
var fbloginURL = 'login/facebook/'

accountsApp.factory('httpServices', function($http, $q, $cookies) 
{
	var loginData = {}
	$http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
	loginData.login_to_fb = function()
	{
		var access_token = $http.post(fbloginURL)
		return $q.all({'access_token':access_token})
	}
	return loginData
});