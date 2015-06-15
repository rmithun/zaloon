//URL
var fbloginURL = '/register/facebook/'
var accountURL  = '/account/'

noqapp.factory('httpServices', function($http, $q, $cookies, sessionService) 
{
	//$http.defaults.headers.common['Authorization'] = sessionService.getAccessToken();
	var loginData = {}

	loginData.getFBKey = function()
	{
		var fb_key = $http.get(accountURL+'fb_key/')
		return $q.all({'fb_key':fb_key})
	}

	loginData.loginUsingFB = function(dummyKey)
	{
		var access_token = $http.post(fbloginURL, dummyKey)
		return $q.all({'access_token':access_token})
	}

	loginData.getUsrDetails = function()
	{
		//$http.defaults.headers.get['Authorization'] = "Bearer " + sessionService.getAccessToken();
		var user_details = $http.get(accountURL+'user_auth/')
		return $q.all({'user_details':user_details})
	}

	loginData.logOut = function()
	{
		var logout = $http.delete(accountURL+"user_auth/")
		return $q.all({'log_out':logout})
	}
	loginData.getDetails = function()
	{
		var booking = $http.get(accountURL+"my_booking")
		var user_details = $http.get(accountURL+'user_details/')
		//var booking_history = $http.get(accountURL+'booking_history/')
		return $q.all({'booking':booking,'user_details':user_details})
	}

    return loginData;
});


noqapp.factory('sessionService', function($q,$cookies)
{
	var sessionData = {}
	sessionData.setAuthToken = function(token)
	{
		$cookies.put('token',token['access_token'].data['access_token']);
		expiretime = new Date()
		//$cookies.expiretime = expiretime.setMinutes(token['access_token'].data['expires_in']);
		//$cookies.refreshtoken = token['access_token'].data['refresh_token'] 
		//$cookies.client_id = token['access_token'].data['client_id']
		//$cookies.client_secret = token['access_token'].data['client_secret']


	}
	sessionData.getAccessToken = function()
	{
		auth_token = $cookies.get('token');
		return auth_token
	}

	sessionData.isLogged = function()
	{
		//check has token
		//check if token no expired
		//if expired get new token using refresh token
		//on logout clear cookies
		if($cookies.get('token') == undefined || $cookies.get('token') == null)
			{
				return false;
			}
		else
			{
				return true;
		}
	}
	return sessionData

})

noqapp.factory('authInterceptor', [
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