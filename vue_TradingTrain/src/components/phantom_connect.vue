<script>
export default {
  //access data from App.vue
  inject: ['walletData'],

  //claim data to store publicWalletAddress
  data() {
    return {
      publicWalletAddress: ''
    }
  },

  //claim data to store publicWalletAddress
  methods: {
    connectPhantom: async function () {
      var vm = this;
      var wallet = this.walletData;

      // if walletData has defined
      if (wallet) {

        // call the function named connect() in walletData;
        const response = await wallet.connect();

        // store the response in publicWalletAddress; use ViewModel vm
        vm.publicWalletAddress = response.publicKey.toString();
      }
    },
    disconnectPhantom: function () {
      var wallet = this.walletData;
      // if walletData has defined

      // call the function named connect() in walletData;
      wallet.disconnect();
      // store the response in publicWalletAddress; use ViewModel vm
      this.publicWalletAddress = '';
    }
  }
}
</script>

<template>
  <div class="container">
    <template v-if="walletData && publicWalletAddress == ''">
      <button class="btn-mg" @click="connectPhantom">
        CONNECT WALLET
      </button>
    </template>

    <template v-if="publicWalletAddress != ''">
      <p class="text-white-mg">
        Welcome to the Solana network, <br />
        <strong>{{ publicWalletAddress }}</strong>
      </p>
      <div class="success_img">
        <img src="../assets/welcome.gif" />
      </div>
      <button class="btn-mg" @click="disconnectPhantom">
        DISCONNECT WALLET
      </button>
    </template>

    <template v-if="walletData == null">
      <div>
        <p>Checking ...</p>
      </div>
      <a href="https://phantom.app/">
        You don't have a Phantom wallet ! Get one there !
      </a>
    </template>
  </div>
</template>

<style scoped>
body {
  background-color: rgba(31, 41, 55, 1);
}

.success_img {
  width: 90%;
}

.success_img img {
  width: 90%;
}
</style>
