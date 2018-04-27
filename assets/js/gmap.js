function initMap() {
  var map = document.querySelector('#map')
  var location = new google.maps.LatLng(48.4295057, 34.9780057)
  var mapInstance = new google.maps.Map(map, {
    zoom: 15,
    center: location
  })
  var mapMarker = new google.maps.Marker({
    position: location
  })
  mapMarker.setMap(mapInstance)
}