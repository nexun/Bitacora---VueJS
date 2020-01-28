<template>
<div class="map">
    <l-map
      v-if="showMap"
      :zoom="zoom"
      :center="center"
      :options="mapOptions"
      @update:center="centerUpdate"
      @update:zoom="zoomUpdate"
      style="position:relative;"
    >
      <l-tile-layer :url="url"  />
      <l-marker :lat-lng="withPopup">       
      
      </l-marker>
      <l-control :position="'bottomleft'" class="custom-control-watermark">
        Grupo 15 - UNLP
      </l-control>
    </l-map>
    <br>
    <br>
</div>    
</template>

<script>
import axios from 'axios'
import { latLng, icon  } from "leaflet";
import { LMap, LTileLayer, LMarker, LControl} from "vue2-leaflet";

export default {
  name: "Ma",
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LControl
  },
  data() {
    
    return {
      latitud: null,
      longitud:null,
      zoom: 15,
      center: latLng(-34.90823,-57.92795),
      withPopup: latLng(47.41322, -1.219482),
      url: "http://{s}.tile.osm.org/{z}/{x}/{y}.png",
      staticAnchor: [16, 37],
      customText: "Foobar",
      iconSize: 64,
      currentZoom: 15,
      currentCenter: latLng(-34.90823,-57.92795),
      mapOptions: {
        zoomSnap: 0.1
      },
      showMap: true
    };
  },
  created() {
        axios.get('/center/' + this.$route.params.id)
            .then(response => {
                this.latitud = response.data.latitude                              
                this.longitud = response.data.longitude
                this.currentCenter =latLng(this.latitud,this.longitud)
                this.center =latLng(this.latitud,this.longitud)
                this.withPopup =latLng(this.latitud,this.longitud)

                          
            })
            .catch(error => {})
    },
   
  methods: {
    zoomUpdate(zoom) {
      this.currentZoom = zoom;
    },
    centerUpdate(center) {
      this.currentCenter = center;
    },
    showLongText() {
      this.showParagraph = !this.showParagraph;
    }    
  }
};
</script>

<style scoped>
.map {
  width: 100%;
  height: 100%;
  padding: 10px; 
  border: 1px solid #c8c5c5;
  border-radius: 8px;
}
.example-custom-control {
  background: #fff;
  padding: 0 0.5em;
  border: 1px solid #aaa;
  border-radius: 0.1em;
}
.custom-control-watermark {
  font-size: 200%;
  font-weight: bolder;
  color: #aaa;
  text-shadow: #555;
}
</style>
