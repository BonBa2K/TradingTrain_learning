import stockInit from 'highcharts/modules/stock'
import Highcharts from 'highcharts'
import HighchartsVue from 'highcharts-vue'
import { createApp } from 'vue'
import App from './App.vue'

stockInit(Highcharts)
const app = createApp(App);
app.use(HighchartsVue)
app.mount("#app");
