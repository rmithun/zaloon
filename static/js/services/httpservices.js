//URL
var fbloginURL = '/register/facebook/'

accountsApp.factory('httpServices', function($http, $q, $cookies) 
{
	var loginData = {}
	loginData.login_to_fb = function(dummyKey)
	{
		var access_token = $http.post(fbloginURL, dummyKey)
		return $q.all({'access_token':access_token})
	}
    return loginData;
});

