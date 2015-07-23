noqapp.factory('genericServices', function($q) 
{	
	var autocompData = {}
	var acService = new google.maps.places.AutocompleteService();
	autocompData.getLocation = function(location)
	{
		console.log(location);
		acService.getPlacePredictions({
                input: location,
                types: ['(regions)'],
                componentRestrictions: { 'country': 'in' }
            }, function (places, status) {
                if (status === google.maps.places.PlacesServiceStatus.OK) {                    
                    var _places = [];                    
                    for (var i = 0; i < places.length; ++i) {
                    	_places.push({
                        	id: places[i].place_id,
                        	value: places[i].description,
                        	label: places[i].description
                    	});
                	} 
                	if(_places != 'undefined')
                	{
	                	return $q.all({'_places':_places})
                	}
            	}
        	});
	}
	return autocompData;
});