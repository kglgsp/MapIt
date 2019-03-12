  function initMap() {
      var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10
      });

      var input = document.getElementById('pac-input');
      var searchBox = new google.maps.places.SearchBox(input);
      map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
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

        // Bias the SearchBox results towards current map's viewport.
    map.addListener('bounds_changed', function() {
      searchBox.setBounds(map.getBounds());
    });

    mainObj = {};

    let showObj = function() {
      for (let prop in mainObj) {
        console.log(prop);
        console.log(mainObj[prop]);
      };
    }
    fetch("./tweets.json")
    .then(function(resp) {
      return resp.json();
    })

    .then(function(data) {
      mainObj = data;
      showObj();

      addMarker({
        coords:{lat:data.place.bounding_box.coordinates[0][1][1],lng:data.place.bounding_box.coordinates[0][1][0]},
        content:'<div id="content">'+
        '<div id="siteNotice">'+
        '</div>'+
        '<h1 id="firstHeading" class="firstHeading">'+data.user.screen_name+'</h1>'+
        '<div id="bodyContent">'+
        '<p>'+data.extended_tweet.full_text+'</p>'+
        '</div>'+
        '</div>'
      });


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
    });

    
  }

  function handleLocationError(browserHasGeolocation, infoWindow, pos) {
      infoWindow.setPosition(pos);
      infoWindow.setContent(browserHasGeolocation ?
                            'Error: The Geolocation service failed.' :
                            'Error: Your browser doesn\'t support geolocation.');
      infoWindow.open(map);
  }

 