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
            bloqueados: 10,
            desbloqueados: 11,
            docentes: 12,            
            series: [],
            chartOptions: {            
                labels: ['Permitidos', 'Bloqueados'],
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
        axios.get('/user_bloqued_cant')
            .then(response => {
                this.desbloqueados = response.data.cant_tot - response.data.cant_bloqued
                this.bloqueados = response.data.cant_bloqued
                
                this.series = [this.desbloqueados,this.bloqueados]
             
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