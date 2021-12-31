<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>map</title>
    <style>
      /* Always set the map height explicitly to define the size of the div
       * element that contains the map. */
      #map {
        height: 100%;
      }
      /* Optional: Makes the sample page fill the window. */
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
    </style>
  </head>
  <body>
    <div id="map"></div>
    <script>

      function initMap() {
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 15,
          center: {lat: 24.1790108, lng: 120.6039384},
          mapTypeId: 'terrain'
        });
		<?php require "sql.php"; ?>
		var yo = <?php echo json_encode($roads); ?>;
		var color = ['#00FF00','#88FF00','#FFFF00','#FF8800','#FF0000','#005CFF','#000000','#FF00FF'];
	for(i=0;i<yo.length;i++)
	if(yo[i][5]<5)
         (new google.maps.Polyline({
          path: [
          {lat: yo[i][1], lng: yo[i][2]},
          {lat: yo[i][3], lng: yo[i][4]}
	  ],
          geodesic: true,
          strokeColor: color[yo[i][5]],
          strokeOpacity: 1.0,
          strokeWeight: 2
        })).setMap(map);
		
      }
    </script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyD_RqSC1FAOKMntanwdIHKCG_QioGDcc3Q&callback=initMap">
    </script>
  </body>
</html>

