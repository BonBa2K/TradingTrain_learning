import Vue from 'vue'
import { createApp } from 'vue'
import App from './App.vue'
import './assets/main.css'
import HighchartsVue from 'highcharts-vue'

Vue.use(HighchartsVue);
createApp(App).mount('#app')
