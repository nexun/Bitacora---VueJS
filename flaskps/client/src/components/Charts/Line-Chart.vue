<template>
<div> 
    <div class="d-inline-flex shadow p-0">   
        <div class="p-1">
            <VueApexCharts type=line width=380 height=239  :options="chartOptions" :series="series" />
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
        series: [{
            name: "Desktops",
            data: [10, 41, 35, 51, 49, 62, 69, 91, 118, 15, 100]
        }],
        chartOptions: {
          chart: {                
                zoom: {
                    enabled: false
                }
            },
            dataLabels: {
                enabled: false
            },
            stroke: {
                curve: 'straight'
            },
            title: {
                text: 'Asistencias por mes',
                align: 'left'
            },
            grid: {
                row: {
                    colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
                    opacity: 0.5
                },
            },
            xaxis: {
                categories: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
            },
            legend: {
                containerMargin: {
                    left: 35,
                    right: 60
                }
            },
            responsive: [{
                breakpoint: 1500,
                options: {
                    chart: {
                        width: 270,
                        height: 250
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