import axios from 'axios';

const instance = axios.create({
  baseURL: process.env.VUE_APP_BACKEND_URL,
  // You can add more default configurations here
});

export default instance;
