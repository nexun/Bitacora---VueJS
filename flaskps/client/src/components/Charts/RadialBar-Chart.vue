<template>
<div> 
    <div class="d-inline-flex shadow p-0">   
        <div class="p-1">
            <VueApexCharts type=radialBar width=380   :options="chartOptions" :series="series" />
        </div>
    </div>    
</div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'



export default {
    name: 'Home',
    components: {
        VueApexCharts,
    },
    data() {
        return {
            series: [70],
            chartOptions: {
                chart: {                
                zoom: {
                    enabled: false
                }
                 },
                plotOptions: {
                    radialBar: {
                        hollow: {
                            size: '60%',
                        }
                    },
                },
          labels: ['Completado'],
          responsive: [{
            breakpoint: 1500,
            options: {
                chart: {
                    width: 270,
                    height: 280
                },
                legend: {
                    position: 'bottom'
                },    
            }
          }]
        }
      }
    }
}
</script>
<style scoped>
.card-header {
    border-bottom: 1px solid #69262c;
}

</style>