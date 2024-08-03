<template>
  <div>
    <h1>Data from Backend</h1>
    <div v-if="data">{{ data }}</div>
    <div v-else>Loading...</div>
  </div>
</template>

<script>
import axios from '@/plugins/axios';

export default {
  data() {
    return {
      data: null
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get('/api/mymodel/');
        //   const response = await axios.get('/api/mymodel');
        this.data = response.data;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }
  }
};
</script>
