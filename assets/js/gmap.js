function initMap() {
  var map = document.querySelector('#map')
  var location = new google.maps.LatLng(25,118)
  var mapInstance = new google.maps.Map(map, {
    zoom: 8,
    center: location
  })
  var mapMarker = new google.maps.Marker({
    position: location
  })
  mapMarker.setMap(mapInstance)
}