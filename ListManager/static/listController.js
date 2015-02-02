/**
 * Created by Ryan on 2/1/15.
 */

console.log("test");

var app = angular.module('myApp', ['ngGrid']);
app.controller('MyCtrl', function($scope, $http) {


    $scope.inputBoxName = "";
    $scope.inputBoxAmount = "";

    $scope.items =
    [
        {name: "Tomates", amount:"10"},
        {name: "Beef Roast", amount:"3 lbs"}
    ];

    $scope.init = function() {
        console.log($scope.items);
    }

    $scope.addItem = function() {
        if ($scope.inputBoxName == "" || $scope.inputBoxAmount == "")
            return;

        $scope.items.push({name:$scope.inputBoxName, amount:$scope.inputBoxAmount});
        $scope.inputBoxName = "";
        $scope.inputBoxAmount = "";
    }

    $scope.deleteItem = function(item) {
        var index = $scope.items.indexOf(item);
        if (index > -1)
            $scope.items.splice(index, 1);
    }

    $scope.print = function() {
        var request = $http({
            method: "post",
            url: "/print/",
            data: $scope.items
        });
    }


});