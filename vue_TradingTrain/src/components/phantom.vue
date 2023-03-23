<script>
import { defineAsyncComponent } from 'vue'
export default {
    inject: ['phantom'],
    data: {
        publicWalletAddress: ""
    }
}
const connectPhantom = async () => {
    if (phantom) {
        console.log('phantom', phantom)
        const response = await phantom.connect();
        publicWalletAddress.value = response.publicKey.toString();
        console.log('Connected with Public Key:', response)
    }
}
</script>