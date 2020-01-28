<template>
<div> 
    <div class="card d-inline-flex shadow p-0">   
        <div class="card-body p-1">   
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
            confirmados: 10,
            noconfirmados: 11,
            docentes: 12,            
            series: [],
            chartOptions: {            
                labels: ['Verificados', 'Sin Verificar'],
                colors : ['#00cc00', '#FF0000'],
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
        axios.get('/user_confirm_cant')
            .then(response => {
                this.confirmados = response.data.cant_confirmed
                this.noconfirmados = response.data.cant_tot - response.data.cant_confirmed
                
                this.series = [this.confirmados,this.noconfirmados]
             
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