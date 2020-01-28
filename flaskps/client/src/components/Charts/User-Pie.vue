<template>
<div> 
    <div class="card d-inline-flex shadow p-0">   
        <div class="card-body p-1 ">  
         <VueApexCharts type=donut width=380  :options="chartOptions" :series="series" />
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
            administradores: 10,
            preceptores: 11,
            docentes: 12,            
            series: [],
            chartOptions: {            
                labels: ['Administradores', 'Preceptores', 'Docentes'],
                colors : ['#00cc00', '#0000FF', '#FF8000'],
                responsive: [{
                    breakpoint: 1800,
                    options: {
                        chart: {
                            width: 250
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
        axios.get('/user_role_cant')
            .then(response => {
                this.administradores = response.data[0].cant
                this.preceptores = response.data[1].cant
                this.docentes = response.data[2].cant
                
                this.series = [this.administradores,this.preceptores,this.docentes]
             
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