// src/router.js
import { comma } from 'postcss/lib/list';
import { createRouter, createWebHistory } from 'vue-router';
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
    path: '/post/',
    name: 'Post',
    component: () => import('./components/Post/index.vue'),
    children: [
      {
        path: '2/',
        name: 'Post2',
        component: () => import('./components/Post/card2.vue')
      },
      {
        path: '1/',
        name: 'Post1',
        component: () => import('./components/Post/card1.vue')
      },
      {
        path: '3/',
        name: 'Post3',
        component: () => import('./components/Post/card3.vue')
      },
      {
        path: '4/',
        name: 'Post4',
        component: () => import('./components/Post/card4.vue')
      },
      {
        path: '5/',
        name: 'Post5',
        component: () => import('./components/Post/card5.vue')
      },
      {
        path: '6/',
        name: 'Post6',
        component: () => import('./components/Post/card6.vue')
      },
      {
        path: '7/',
        name: 'Post7',
        component: () => import('./components/Post/card7.vue')
      },
      {
        path: '8/',
        name: 'Post8',
        component: () => import('./components/Post/card8.vue')
      }
    ]
  },
  {
    path: '/p9/',
    name: 'Post9',
    component: () => import('./components/Post/card9.vue')
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
    path: '/knowledge/',
    name: 'knowledge',
    component: () => import('./components/jiajiao/knowledge/index.vue')
  },
  {
    path: '/profile/',
    name: 'profile',
    component: () => import('./components/jiajiao/Profile.vue')
  },
  {
    path: '/me/',
    name: 'Me',
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
  history: createWebHistory(),
  routes
});

export default router;
