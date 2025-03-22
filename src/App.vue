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
      <!-- 返回按钮 -->
      <v-btn
        variant="text"
        @click.stop="goBack"
        prepend-icon="mdi-arrow-left"
        text="返回"
      />
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <!-- <v-btn @click="toggleTheme">toggle theme</v-btn> -->
      <v-btn
        @click.stop="go2Explore"
        variant="text"
        prepend-icon="mdi-compass-outline"
        class="hidden-xs"
      >
        探索
      </v-btn>
      <v-btn
        @click.stop="go2jiajiao"
        variant="text"
        prepend-icon="mdi-school"
        class="hidden-xs"
      >
        家教
      </v-btn>
      <v-btn
        @click.stop="go2nearby"
        variant="text"
        prepend-icon="mdi-map-marker"
        class="hidden-xs"
      >
        附近
      </v-btn>
      <v-btn
        @click.stop="go2about"
        variant="text"
        prepend-icon="mdi-information"
        class="hidden-xs"
      >
        关于我
      </v-btn>
      <v-btn
        @click.stop="go2Me"
        variant="text"
        prepend-icon="mdi-account"
        class="hidden-xs"
      >
        个人信息
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

    <!-- 只在移动端显示底部导航栏 -->
    <v-bottom-navigation :elevation="24" class="d-md-none">
      <v-btn value="" @click="go2Recent">
        <v-icon>mdi-compass-outline</v-icon>
        <span>探索</span>
      </v-btn>

      <v-btn value="jiajiao" @click.stop="go2jiajiao">
        <v-icon>mdi-school</v-icon>
        <span>家教</span>
      </v-btn>

      <v-btn value="nearby" @click.stop="go2nearby">
        <v-icon>mdi-map-marker</v-icon>
        <span>附近</span>
      </v-btn>

      <v-btn value="me" @click.stop="go2Me">
        <v-icon>mdi-account</v-icon>
        <span>我</span>
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
    goBack() {
      this.$router.go(-1);
    },
    go2Recent() {
      this.$router.push({
        name: 'Explore'
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
        name: 'Profile'
      });
    },
    go2about() {
      this.$router.push({
        name: 'About'
      });
    },
    go2Explore() {
      this.$router.push({
        name: 'Explore'
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

<style scoped>
/* 在中等尺寸及以上的设备隐藏 */
@media (min-width: 960px) {
  .d-md-none {
    display: none !important;
  }
}

/* 在小尺寸设备上隐藏 */
@media (max-width: 599px) {
  .hidden-xs {
    display: none !important;
  }
}
</style>
