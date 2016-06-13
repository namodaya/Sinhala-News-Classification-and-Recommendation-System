SNCR_app.controller("commonController", function ($scope, $http, $filter) {


    $scope.getNews = function (category) { // Getting News Data from DB
        var url = 'http://127.0.0.1:5000/category/' + category;
        $http
            .get(url)
            .then(function (resp) {
                    $scope.items = resp.data;
                    console.log($scope.items);
                },
                function (err) {
                    console.log('Item request ERR ' + err);
                })
    };
    console.log("common is running");

});