<template>
<div> 
    <div class="d-inline-flex shadow p-0">   
        <div class="p-1">
            <VueApexCharts type=donut width=380 height=280  :options="chartOptions" :series="series" />
        </div>
    </div>    
</div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
import axios from 'axios'

export default {
    name: 'Home',
    components: {
        VueApexCharts,
    },
    
    data() {
        return {
            amarillo: 10,
            azul: 11,
            naranja: 12,
            rojo: 13,
            rosa: 22,
            verde: 22,
            sin_nivel:22,
            series: [],
            chartOptions: {            
                labels: ['Amarillo', 'Azul', 'Naranja', 'Rojo', 'Rosa','Verde','Sin Nivel'],
                colors : ['#FFF014', '#0000FF', '#FF8000', '#FF0000', '#FF759E','#40FF4D','#00E396'],
                responsive: [{
                    breakpoint: 1500,
                    options: {
                        chart: {
                            width: 270,
                            height: 259,
                        },
                        legend: {
                            position: 'bottom'
                        },    
                    }
                }]
            }
      }
    },
    created() {
        axios.get('/level_cant')
            .then(response => {
                this.amarillo = response.data[0].cant
                this.azul = response.data[1].cant
                this.naranja = response.data[2].cant
                this.rojo = response.data[3].cant
                this.rosa = response.data[4].cant
                this.sin_nivel = response.data[5].cant
                this.verde = response.data[6].cant
                this.series = [this.amarillo,this.azul,this.naranja,this.rojo,this.rosa,this.verde,this.sin_nivel]
             
            })
            .catch(error => {})
    }    
}
</script>

<style scoped>
.card-header {
    border-bottom: 1px solid #69262c;
}
</style>