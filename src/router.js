// src/router.js
import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './components/HelloWorld.vue';
const notebookNames = ['n1', 'n2', 'n3']; // Add more notebook names as needed
// Initialize the routes array with the Home route
const routes = [
    {
      path: '/',
      name: 'Home',
      component: HomePage
    }
  ];
// Loop through the notebook names to create route objects
notebookNames.forEach(name => {
    routes.push({
      path: `/${name}/`,
      name: name,
      component: () => import(`./components/notebooks/${name}.vue`) // Adjust the path as needed
    });
  });
  
const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;