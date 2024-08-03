<template>
  <v-container fluid >
    <v-row justify="end" align="center">
      <v-col cols="2">
        <v-card color="blue lighten-4" class="pa-5" :style="{height:'300px'}">
          <div class="text-center">Centered Box 1</div>
        </v-card>
      </v-col>
      <v-col cols="2">
        <v-card color="green lighten-4" class="pa-5">
          <div class="text-center">Centered Box 2</div>
        </v-card>
      </v-col>
      <v-col cols="2">
        <v-card color="green lighten-4" class="pa-5">
          <div class="text-center">Centered Box 2</div>
        </v-card>
      </v-col>
      <!-- <v-col cols="1">
          <v-card color="green lighten-4" class="pa-5">
            <div class="text-center">Centered Box 2</div>
          </v-card>
        </v-col> -->
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'SimpleLayoutDemo'
};
</script>

<style>
html,
body,
#app {
  height: 100%;
  margin: 0;
}
.fill-height {
  height: 100%;
}
</style>
