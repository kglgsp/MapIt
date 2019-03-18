  function initMap() {
      var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 9
      });

      var geocode = new google.maps.Geocoder;
      var infoWindow = new google.maps.InfoWindow;


        if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(function(position) {
            var pos = {
              lat: position.coords.latitude,
              lng: position.coords.longitude
            };

            infoWindow.setPosition(pos);
            infoWindow.setContent('Current Location');
            infoWindow.open(map);
            map.setCenter(pos);
          }, function() {
            handleLocationError(true, infoWindow, map.getCenter());
          });
        } else {
          // Browser doesn't support Geolocation
          handleLocationError(false, infoWindow, map.getCenter());
        }

    mainObj = {};
    var arrayTweet = [];

    let showObj = function() {
      for (let prop in mainObj) {

      addMarker({
        coords:{lat:mainObj[prop]["_source"]["coordinates"]["lat"],
                lng:mainObj[prop]["_source"]["coordinates"]["lon"]},
        content:'<div id="content">'+
        '<div id="siteNotice">'+
        '</div>'+
        '<b>'+mainObj[prop]["_source"]["screen_name"]+'</b>'+
        '<div id="bodyContent">'+
        '<p>'+mainObj[prop]["_source"]["text"]+'</p>'+
        '<p>'+mainObj[prop]["_score"]+'</p>'+
        '</div>'+
        '</div>'
      });

      // Removes the markers from the map, but keeps them in the array.
      function clearMarkers() {
        setMapOnAll(null);
      }

      // Add Marker Function
      function addMarker(props){
        var marker = new google.maps.Marker({
          position:props.coords,
          map:map
        });

        // Check content
        if(props.content){
          var infoWindow = new google.maps.InfoWindow({
            content:props.content
          });

          marker.addListener('click', function(){
            infoWindow.open(map, marker);
          });
        }

      }
      };
    }
    
    fetch("./q.json")
    .then(function(resp) {
      return resp.json();
    })

    .then(function(data) {
      mainObj = data["hits"]["hits"];
      console.log(mainObj)
      showObj();
    });
  }

  function handleLocationError(browserHasGeolocation, infoWindow, pos) {
      infoWindow.setPosition(pos);
      infoWindow.setContent(browserHasGeolocation ?
                            'Error: The Geolocation service failed.' :
                            'Error: Your browser doesn\'t support geolocation.');
      infoWindow.open(map);
  }
  

//   function test() {
//     var query = document.getElementById("site-search").value

//      var data = {
//        query: {
//          bool: {
//            must: {
//              term: {text: query}
//            }
//          }
//        }
//      }
 
//      $.ajax({
//        type: "POST",
//        url: "http://localhost:9200/locations/_search",
//        data: JSON.stringify(data),
//        contentType: 'application/json',
//      })
//      .done(function( data ) {
//        console.log(data);
//      })
//      .fail(function( data ) {
//        console.log(data);
//      });
//  }