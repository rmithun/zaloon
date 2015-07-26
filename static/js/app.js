var noqapp = angular.module('accountApp', ['ngCookies','ngRoute','ui.bootstrap','ngLodash']);

noqapp.run(function($http,$cookies,sessionService) {

	$http.defaults.headers.post['X-CSRFToken'] = $cookies.get('csrftoken');

});

// configure our routes
noqapp.config(function($routeProvider,$httpProvider) {

	$httpProvider.interceptors.push('authInterceptor');

		$routeProvider
			// route for the home page
			.when('/', {
				templateUrl : '/home/',
				controller  : 'homepagecontroller'
			})
			
			.when('/search', {
				templateUrl : '/search/',
				controller  : 'resultCtrl'
			})

			.when('/my_account', {
				templateUrl : '/account/user_account/',
				controller  : 'accountscontroller'
			})

			.when('/home', {
				templateUrl : '/home/',
				controller  : 'homepagecontroller'
			})

			.when('/booking', {
				templateUrl : '/booking/booking_page/'
			})

});
