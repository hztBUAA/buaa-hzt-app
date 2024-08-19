<template>
  <v-app>
    <v-app-bar
      color="primary"
      density
      image="https://picsum.photos/1920/1080?random"
    >
      <template v-slot:image>
        <v-img
          gradient="to top right, rgba(19,84,122,.8), rgba(128,208,199,.8)"
        ></v-img>
      </template>
      <template v-slot:prepend>
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
      </template>
      <v-app-bar-title>Hzt's Site</v-app-bar-title>
      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>

    <v-bottom-navigation :elevation="24">
      <v-btn value="recent" @click="go2Recent">
        <v-icon>mdi-history</v-icon>

        <span>Recent</span>
      </v-btn>

      <v-btn value="favorites" @click.stop="go2Favorites">
        <v-icon>mdi-heart</v-icon>

        <span>Favorites</span>
      </v-btn>

      <v-btn value="me" @click.stop="go2Me">
        <v-icon>mdi-map-marker</v-icon>

        <span>Me</span>
      </v-btn>
    </v-bottom-navigation>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld';

export default {
  name: 'App',

  components: {
    HelloWorld
  },

  data: () => ({
    //
  }),
  methods: {
    go2Recent() {
      this.$router.push({
        name: 'Post'
      });
    },
    go2Favorites() {
      this.$router.push({
        name: 'Favorites'
      });
    },
    go2Me() {
      this.$router.push({
        name: 'Me'
      });
    }
  }
};
</script>
