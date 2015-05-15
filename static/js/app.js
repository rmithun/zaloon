var accountsApp = angular.module('accountApp', ['ngCookies']);

accountsApp.run(function($http,$cookies) {
	$http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
});

