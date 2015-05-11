var my_app=angular.module('MyApp', ['uiGmapgoogle-maps']);

	my_app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
	});
	my_app.config(function(uiGmapGoogleMapApiProvider) {
    uiGmapGoogleMapApiProvider.configure({
        //    key: 'your api key',
        v: '3.17',
        libraries: 'weather,geometry,visualization'
    });
})
   my_app.controller('MapController', function($scope, uiGmapGoogleMapApi){
   		$scope.map = { center: { latitude: 45, longitude: -73 }, zoom: 8 };

   		uiGmapGoogleMapApi.then(function(maps) {
   			console.log(maps)
    	});
   }); 
