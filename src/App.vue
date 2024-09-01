<template>
  <v-app>
    <v-app-bar color="primary" density image="https://picsum.photos/1920/1080">
      <template v-slot:image>
        <v-img
          gradient="to top right, rgba(19,84,122,.8), rgba(128,208,199,.8)"
        ></v-img>
      </template>
      <template v-slot:prepend>
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
      </template>
      <v-app-bar-title>HZT小站</v-app-bar-title>
      <!-- <v-btn @click="toggleTheme">toggle theme</v-btn> -->
      <v-btn
        @click.stop="go2Posts"
        variant="text"
        prepend-icon="mdi-post-outline"
      >
        动态
      </v-btn>
      <v-btn
        @click.stop="go2nearby"
        variant="text"
        prepend-icon="mdi-account-multiple"
      >
        附近
      </v-btn>
      <v-btn
        @click.stop="go2about"
        variant="text"
        prepend-icon="mdi-information"
      >
        关于
      </v-btn>
      <v-btn href="http://github.com/hztBUAA" prepend-icon="mdi-github">
        github
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <!-- <v-overlay>
        <template #activator="{ isActive, props }">
          <v-btn v-bind="props" block
            >Overlay is {{ isActive ? 'open' : 'closed' }}</v-btn
          >
        </template>
      </v-overlay> -->
      <router-view></router-view>
    </v-main>

    <v-bottom-navigation :elevation="24">
      <v-btn value="" @click="go2Recent">
        <v-icon>mdi-history</v-icon>

        <span>探索</span>
      </v-btn>

      <v-btn value="favorites" @click.stop="go2Favorites">
        <v-icon>mdi-heart</v-icon>

        <span>猜你喜欢</span>
      </v-btn>
      <v-btn value="jiajiao" @click.stop="go2jiajiao">
        <v-icon>mdi-school</v-icon>

        <span>家教</span>
      </v-btn>

      <v-btn value="me" @click.stop="go2Me">
        <v-icon>mdi-map-marker</v-icon>

        <span>我的</span>
      </v-btn>
    </v-bottom-navigation>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld';
import { useTheme } from 'vuetify';
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
    go2jiajiao() {
      this.$router.push({
        name: 'jiajiao'
      });
    },
    go2Me() {
      this.$router.push({
        name: 'Me'
      });
    },
    go2about() {
      this.$router.push({
        name: 'About'
      });
    },
    go2Posts() {
      this.$router.push({
        name: 'Post'
      });
    },
    go2nearby() {
      this.$router.push({
        name: 'nearby'
      });
    },
    toggleTheme() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
    }
  }
};
</script>
