<template>
    <highcharts class="chart" :options="chartOptions"></highcharts>
</template>
<script>
export default {
    data() {
        return {
            chartOptions: {
                chart: {
                    type: 'line'
                },
                title: {
                    text: 'Fruit Consumption'
                },
                xAxis: {
                    categories: ['Apples', 'Bananas', 'Oranges']
                },
                yAxis: {
                    title: {
                        text: 'Fruit eaten'
                    }
                },
                series: [{
                    name: 'Jane',
                    data: [1, 0, 4]
                }, {
                    name: 'John',
                    data: [5, 7, 3]
                }]
            },
        }
    }
}
</script>