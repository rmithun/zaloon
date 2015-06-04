var accountsApp = angular.module('accountApp', ['ngCookies','ngRoute']);

accountsApp.run(function($http,$cookies) {

	$http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];

});

// configure our routes
accountsApp.config(function($routeProvider,$httpProvider) {
	$httpProvider.interceptors.push('authInterceptor');
		$routeProvider
			// route for the home page
			.when('/', {
				templateUrl : '/account/search/'
			})
			
			.when('/search', {
				templateUrl : '/account/search/'
			})

});
