//URL
var fbloginURL = '/register/facebook/'
var accountURL  = '/account/'

accountsApp.factory('httpServices', function($http, $q, $cookies) 
{
	var loginData = {}
	loginData.loginUsingFB = function(dummyKey)
	{
		var access_token = $http.post(fbloginURL, dummyKey)
		return $q.all({'access_token':access_token})
	}

	loginData.getUsrDetails = function()
	{
		var user_details = $http.get(accountURL+'user_details/')
		return $q.all({'user_details':user_details})
	}
    return loginData;
});


accountsApp.factory('sessionService', function($q)
{
	var sessionData = {}
	var auth_token = ''
	sessionData.setAuthToken = function(token)
	{
		auth_token = token
	}
	sessionData.getAccessToken = function()
	{
		return auth_token['auth_token'];
	}

	sessionData.isLogged = function()
	{
		if(auth_token['auth_token'] != null){return true;}
		else{return false;}
	}
	return sessionData

})