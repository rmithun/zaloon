var accountsApp = angular.module('accountApp', ['ngCookies','ngRoute']);

accountsApp.run(function($http,$cookies,$injector,sessionService) {
	$http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
	if(sessionService.isLogged())
	{
		$http.defaults.headers.post['Authorization'] = "Bearer " + sessionService.getAccessToken();
	}
});

// configure our routes
accountsApp.config(function($routeProvider) {
		$routeProvider
			// route for the home page
			.when('/', {
				templateUrl : '/account/search/'
			})
			
			.when('/search', {
				templateUrl : '/account/search/'
			})

});
