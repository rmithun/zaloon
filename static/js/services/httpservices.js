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


accountsApp.factory('sessionService', function($q)
{
	var sessionData = {}
	var auth_token = ''
	sessionData.setAuthToken = function(token)
	{
		auth_token =  token['access_token'].data['access_token']

	}
	sessionData.getAccessToken = function()
	{
		return auth_token
	}

	sessionData.isLogged = function()
	{
		if(auth_token != null){return true;}
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