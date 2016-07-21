var markers = [];

function renderMap(checkboxID){

  $.ajax({
      url: "http://localhost:8000/api/trucks?description=" + checkboxID ,
      type: 'GET',
      headers : {Accept: 'application/json'},
      dataType: 'json',
      success:function(data) {
          data.features.forEach(function (obj) {
          
          var marker = new google.maps.Marker({
              position: new google.maps.LatLng(obj.properties.latitude, obj.properties.longitude),
              map: map,
              title: "description"
              });
          markers.push(marker);

          var content = '<div class="infowindow"><b>' + obj.properties.applicant + '</b></div>' 
          + '<div class="infowindow">' + obj.properties.address + '</div>' 
          + '<div class="infowindow">' + obj.properties.fooditems + '</div>' 
          + '<div class="infowindow">' + obj.properties.dayshours + '</div>' 
          + '<div class="infowindow">' + obj.properties.permit_exp + '</div>'
          + '<div class="infowindow">' + obj.properties.latitude + '</div>'
          + '<div class="infowindow">' + obj.properties.longitude + '</div>';

            var infowindow = new google.maps.InfoWindow();
            // add a click event listener when the user clicks on a marker to display the infowindow
            google.maps.event.addListener(marker, 'click', (function (marker, content, infowindow) {
                return function () {
                    // close the previous info-window
                    closeInfos();
                    infowindow.setContent(content);
                    infowindow.open(map, marker);
                    // keep the handle, in order to close it on next click event
                    infos[0] = infowindow;
                };
            })(marker, content, infowindow));
        });
    }
  });
}

function geolocate(latitude, longitude){

  $.ajax({


      url: "http://localhost:8000/api/trucks/nearest/",
      type: 'GET',
      headers : {Accept: 'application/json'},
      dataType: 'json',
      data: { latitude: latitude, longitude: longitude},

      success:function(data) {
          data.features.forEach(function (obj) {
          console.log();
          var marker = new google.maps.Marker({
              position: new google.maps.LatLng(obj.properties.latitude, obj.properties.longitude),
              map: map,
              title: "description"
              });
        });
      }
});
}


function showLocation(position) {
  var latitude = position.coords.latitude;
  var longitude = position.coords.longitude;

  geolocate(latitude, longitude);
}

function errorHandler(err) {
  if(err.code == 1) {
     alert("Error: Access is denied!");
  }
  
  else if( err.code == 2) {
     alert("Error: Position is unavailable!");
  }
}

function getLocation(){

  if(navigator.geolocation){
     // timeout at 60000 milliseconds (60 seconds)
     var options = {timeout:60000};
     navigator.geolocation.getCurrentPosition(showLocation, errorHandler, options);
  }
  
  else{
     alert("Sorry, browser does not support geolocation!");
  }
}



var center = new google.maps.LatLng(37.773972, -122.431297);
    var mapOptions = {
      zoom: 14,
      center: center
    };
    var map = new google.maps.Map(document.getElementById("map"), mapOptions);

    var infos = [];


    function closeInfos() {
        if (infos.length > 0) {
            // detach the info-window from the marker ... undocumented in the API docs
            infos[0].set("marker", null);
            // and close it
            infos[0].close();
            // blank the array
            infos.length = 0;
        }
    }

    // function removeLayer(checkboxID) {
    //   map.removeLayer(vectorLayer);
    // }

    renderMap();



//----Event Listeners---------------------------------------------------------//
$(document).ready(function() {
  //----Checkbox event listener----//
  $(":checkbox").change(function(event) {
    var id = event.currentTarget.id;
  renderMap(id);

  });

  
  //----Menu Flyout----//
  $("#menu-toggle").click(function(evt) {
    evt.preventDefault();
    $("#wrapper").toggleClass("toggled");
  });
  
  // Sets the map on all markers in the array.
  function setMapOnAll(map) {
    for (var i = 0; i < markers.length; i++) {
      markers[i].setMap(map);
    }
  }

  // Removes the markers from the map, but keeps them in the array.
  function clearMarkers() {
    setMapOnAll(null);
  }

  // Shows any markers currently in the array.
  function showMarkers() {
    setMapOnAll(map);
  }

  // Deletes all markers in the array by removing references to them.
  function deleteMarkers() {
    clearMarkers();
    markers = [];
  }

  //---Violent Crime Mapper----//
  //KS: TODO: THERE SHOULD BE A LESS HACKY WAY TO DO THIS.
  // $('#violence').click(function() {
  //   $(".loader").fadeOut("slow");
  //   $(':checkbox').prop('checked', false);
  //   $("[id='Aggravated Assault']").prop('checked', true);
  //   renderMap('Aggravated Assault');
  //   $('#Homicide').prop('checked', true);
  //   renderMap('Homicide');
  //   $('#Rape').prop('checked', true);
  //   renderMap('Rape')
  //   $('#Robbery').prop('checked', true);
  //   renderMap('Robbery');
  // });
  
  //----Clear all selections----/
  //KS: HACK ALERT
  $('#clear').click(function(){
    $(':checkbox').prop('checked', false);
    deleteMarkers();
    });

  });
