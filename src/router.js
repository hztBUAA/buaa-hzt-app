// src/router.js
import { createRouter, createWebHashHistory } from 'vue-router';
// import HomePage from './components/HelloWorld.vue';
// const notebookNames = ['n1', 'n2', 'n3']; // Add more notebook names as needed
const num = 10;
const notebookNames = [];

for (let i = 1; i <= num; i++) {
  notebookNames.push(`n${i}`);
}

// Initialize the routes array with the Home route
const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('./components/Explore/index.vue')
  },
  {
    path: '/explore/',
    name: 'Explore',
    component: () => import('./components/Explore/index.vue')
  },
  {
    path: '/snackbar/',
    name: 'Snackbar',
    children: [
      {
        path: '1/',
        name: 'Snackbar1',
        component: () => import('./components/Snackbar/1.vue')
      }
    ]
  },
  {
    path: '/favorites/',
    name: 'Favorites',
    component: () => import('./components/Favorites/index.vue')
  },
  {
    path: '/jiajiao/',
    name: 'jiajiao',
    component: () => import('./components/jiajiao/index.vue')
  },
  {
    path: '/me/',
    name: 'Profile',
    component: () => import('./components/Me/index.vue')
  },
  {
    path: '/about/',
    name: 'About',
    component: () => import('./components/about/index.vue')
  },
  {
    path: '/nearby/',
    name: 'nearby',
    component: () => import('./components/nearby/index.vue')
  }
];

// Loop through the notebook names to create route objects
notebookNames.forEach((name) => {
  routes.push({
    path: `/${name}/`,
    name: name,
    component: () => import(`./components/notebooks/${name}.vue`) // Adjust the path as needed
  });
});

//-------------------------------------------------------------Login-------------------------------------
// Loop from 1 to 10 to create route objects for each 1.vue to 10.vue
for (let i = 1; i <= 10; i++) {
  routes.push({
    path: `/login/${i}/`,
    name: `Login${i}`,
    component: () => import(`./components/Login/${i}.vue`)
  });
}
//-------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------Chips-------------------------------------
// Loop from 1 to 10 to create route objects for each 1.vue to 10.vue
for (let i = 1; i <= 10; i++) {
  routes.push({
    path: `/chips/${i}/`,
    name: `Chip${i}`,
    component: () => import(`./components/Chips/${i}.vue`)
  });
}
//-------------------------------------------------------------------------------------------------------

const router = createRouter({
  history: createWebHashHistory(),
  routes
});

export default router;
