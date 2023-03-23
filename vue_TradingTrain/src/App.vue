<script>
import HelloWorld from './components/HelloWorld.vue'
const { solana } = window;
var phantom_input;

if (solana?.isPhantom) {
  phantom_input = solana;
}
else {
  phantom_input = null;
}

export default {
  components: {
    HelloWorld,
  },
  provide() {
    return {
      phantom: phantom_input
    }
  }
}
</script>

<template>
  <HelloWorld />
</template>