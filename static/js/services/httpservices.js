//URL
var fbloginURL = '/register/facebook/'
var accountURL  = '/account/'

accountsApp.factory('httpServices', function($http, $q, $cookies, sessionService) 
{

	var loginData = {}
	loginData.loginUsingFB = function(dummyKey)
	{
		var access_token = $http.post(fbloginURL, dummyKey)
		return $q.all({'access_token':access_token})
	}

	loginData.getUsrDetails = function()
	{
		//$http.defaults.headers.get['Authorization'] = "Bearer " + sessionService.getAccessToken();
		var user_details = $http.get(accountURL+'user_details/')
		return $q.all({'user_details':user_details})
	}
    return loginData;
});


accountsApp.factory('sessionService', function($q,$cookies)
{
	var sessionData = {}
	sessionData.setAuthToken = function(token)
	{
		$cookies.token = token['access_token'].data['access_token'];
		expiretime = new Date()
		$cookies.expiretime = expiretime.setMinutes(token['access_token'].data['expires_in']);

	}
	sessionData.getAccessToken = function()
	{
		auth_token = $cookies.token;
		console.log(auth_token)
		return auth_token
	}

	sessionData.isLogged = function()
	{
		//check has token
		//check if token no expired
		//if expired get new token using refresh token
		//on logout clear cookies
		console.log($cookies.token)
		if($cookies.token != null)
			{
				date_ = new Date()
				if($cookies.expiretime >  date_.getTime())
				{
					//make refresh token call
				}
				return true;
			}
		else{return false;}
	}
	return sessionData

})

accountsApp.factory('authInterceptor', [
  "$q", "$window", "$location","sessionService", function($q, $window, $location, sessionService) {
    return {
      request: function(config) {
        config.headers = config.headers || {};
        if(sessionService.isLogged()) 
        {
	        config.headers.Authorization = 'Bearer ' + sessionService.getAccessToken(); // add your token from your service or whatever
        }
        return config;
      },
      response: function(response) {
        return response || $q.when(response);
      },
      responseError: function(rejection) {
        // your error handler
      }
    };
  }
]);