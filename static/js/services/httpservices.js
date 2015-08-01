//URL
var fbloginURL = '/register/facebook/'
var accountURL  = '/account/'
var studioURL = '/studios/'
var bookingURL = '/booking/'

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
		//$http.defaults.headers.get['Authorization'] = "Bearer " + sessionService.getAccessToken();
		var booking = $http.get(bookingURL+"my_booking/")
		var user_details = $http.get(accountURL+'user_details/')
		//var booking_history = $http.get(accountURL+'booking_history/')
		return $q.all({'booking':booking,'user_details':user_details})
	}
	loginData.getService=function()
	{
		var service=$http.get(studioURL+"services/")
		return $q.all({'service_details':service})
	}
	loginData.getstudioDetails=function(req){
		console.log(req);
		var studiodetails=$http.get(studioURL+"studio_profile/",{params:req})
		return $q.all({'studio_details':studiodetails})
	}

	loginData.getstudioTypes=function(){
		var studio_types=$http.get(studioURL+"studio_type/")
		return $q.all({'studio_types':studio_types})
	}

	loginData.getstudioKinds=function(){
		var studio_kinds=$http.get(studioURL+"studio_kind/")
		return $q.all({'studio_kinds':studio_kinds})
	}

	loginData.newBooking=function(booking_data){
		var new_booking=$http.post(bookingURL+"new_booking/",booking_data)
		return $q.all({'new_booking':new_booking})
	}

	loginData.updateBooking=function(payment_resp){
		var update_booking=$http.put(bookingURL+"new_booking/",payment_resp)
		return $q.all({'update_booking':update_booking})
	}

	loginData.updateUserProfile=function(usr_data){
		var update_profile=$http.put(accountURL+"user_details/",usr_data)
		return $q.all({'update_profile':update_profile})
	}

	loginData.getSlots=function(slot_data){
		var available_slots=$http.get(bookingURL+"get_slots/",{params:slot_data})
		return $q.all({'available_slots':available_slots})
	}

	loginData.cancelBooking=function(booking_id){
		var cancel_booking = $http.put(bookingURL+"cancel_booking/",booking_id)
		return $q.all({'cancel_booking':cancel_booking})
	}

	loginData.addReview=function(review_data){
		var add_review = $http.post(bookingURL+"add_review/",review_data)
		return $q.all({'add_review':add_review})
	}

	loginData.applyCoupon = function(coupondata)
	{
		var apply_coupon = $http.get(bookingURL+"apply_coupon/",{params:coupondata})
		return $q.all({'apply_coupon':apply_coupon})
	}

	loginData.splitBookings = function(bookings)
	{
		var active_booking = [], inactive_booking = [];
		for(i=0;i<bookings.length;i++)
		{
			if(bookings[i].booking_status == 'BOOKED' && bookings[i].status_code == 'B001')
			{
				active_booking.push(bookings[i])
			}
			else
			{
				inactive_booking.push(bookings[i])
			}
		}

		return $q.all({'active_booking':active_booking,'inactive_booking':inactive_booking})
	}

    return loginData;
});


noqapp.factory('sessionService', function($q,$cookies)
{
	var sessionData = {}
	sessionData.setAuthToken = function(token)
	{
		$cookies.put('token',token['access_token'].data['access_token'],{path:'/'});
		expiretime = new Date()
		$cookies.put('expiretime',token['access_token'].data['expire_time'],{path:'/'});
		$cookies.put('refreshtoken',token['access_token'].data['refresh_token'],{path:'/'})
		$cookies.put('client_id',token['access_token'].data['client_id'],{path:'/'})
		$cookies.put('client_secret', token['access_token'].data['client_secret'],{path:'/'})


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
	        config.headers.Authorization = 'Bearer ' + sessionService.getAccessToken(); // add your token from your service 
        	//config.headers.Authorization = 'Bearer ' + 'rtPmqphRY60xPVbUO1gDYYZVYx0DE5';
        }
        return config;
      },
      response: function(response) {
        return response || $q.when(response);
      },
      responseError: function(rejection) {
        // your error handler
        return $q.reject(rejection);
      }
    };
  }
]);