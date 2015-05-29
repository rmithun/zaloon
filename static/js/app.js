var accountsApp = angular.module('accountApp', ['ngCookies']);

accountsApp.run(function($http,$cookies,$injector,sessionService) {
	$http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
	if(sessionService.isLogged())
	{
		$http.defaults.headers.post['Authorization'] = "Bearer " + sessionService.getAccessToken();
	}
});

