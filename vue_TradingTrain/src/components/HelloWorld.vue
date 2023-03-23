<script>
export default {
  inject: ['phantom'],
  data() {
    return {
      publicWalletAddress: "",
      phantom: this.phantom,
    }
  },
  methods: {
    connectPhantom: async () => {
      var phantom_de;
      if (phantom) {
        (phantom_de = phantom.solana);
        console.log('phantom_de', phantom_de);
        const response = await phantom_de.connect();
        console.log('Connected with Public Key:', response.publicKey.toString())
        this.publicWalletAddress = response.publicKey.toString();
      }
    }
  }
}
</script>

<template>
  <div id="main-container">
    <template v-if="phantom && !publicWalletAddress">
      <button class="btn-mg" @click="connectPhantom">
        CONNECT WALLET
      </button>
    </template>

    <template v-if="publicWalletAddress">
      <div>
        <p class="text-white-mg">
          Welcome to the Solana network, <br />
          <strong>{{ publicWalletAddress }}</strong>
        </p>
        <div>
          <img src="static/images/welcome.gif" alt="welcome gif" />
        </div>
      </div>
    </template>

    <template v-if="phantom === null">
      <div class="no-phantom-wallet-container">
        <div>
          <div class="lds-dual-ring"></div>
          <p>Checking ...</p>
        </div>
        <a href="https://phantom.app/" target="_blank">
          You don't have a Phantom wallet ! Get one there !
        </a>
      </div>
    </template>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {

  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
