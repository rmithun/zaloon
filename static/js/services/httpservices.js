//URL
var fbloginURL = '/login/facebook/'

accountsApp.factory('httpServices', function($http, $q, $cookies) 
{
	var loginData = {}
	loginData.login_to_fb = function()
	{
		var access_token = $http.get(fbloginURL)
		return $q.all({'access_token':access_token})
	}
	return loginData
});