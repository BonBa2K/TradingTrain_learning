<script>
import phantom_connect from './components/phantom_connect.vue'
// Destructuring the data named solana from window
const { solana: solanaData } = window;
var phantom_input;

// Optional chaining
// if solanaData contain isPhantom attribute  
if (solanaData?.isPhantom) {
  phantom_input = solanaData;
}
else {
  phantom_input = null;
}

export default {

  // import components
  components: {
    phantom_connect,
  },

  // provide data to grand child
  // use inject to access
  provide() {
    return {
      walletData: phantom_input
    }
  }
}
</script>

<template>
  <phantom_connect />
</template>
