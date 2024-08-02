<template>
  <div>
    <!-- <v-navigation-drawer :width="279">
      <v-list-item title="My Application" subtitle="Vuetify"></v-list-item>
      <v-divider></v-divider>
      <v-list-item link title="List Item 1"></v-list-item>
      <v-list-item link title="List Item 2"></v-list-item>
      <v-list-item link title="List Item 3"></v-list-item>
    </v-navigation-drawer> -->
    



    <v-container class="bg-surface-variant mb-6 mt-10">
      <v-row align="start" style="height: 150px" no-gutters>
        <v-col v-for="n in 3" :key="n">
          <v-sheet class="pa-2 ma-2"> .align-start </v-sheet>
        </v-col>
      </v-row>
    </v-container>

    <v-container class="bg-surface-variant mb-6">
      <v-row align="center" style="height: 150px" no-gutters>
        <v-col v-for="n in 4" :key="n">
          <v-sheet class="pa-2 ma-2"> .align-center </v-sheet>
        </v-col>
      </v-row>
    </v-container>

    <v-container class="bg-surface-variant mb-6">
      <v-row align="end" style="height: 150px" no-gutters>
        <v-col v-for="n in 3" :key="n">
          <v-sheet class="pa-2 ma-2"> .align-end </v-sheet>
        </v-col>
      </v-row>
    </v-container>

    <v-container class="bg-surface-variant">
      <v-row style="height: 150px" no-gutters>
        <v-col align-self="start">
          <v-sheet class="pa-2 ma-2"> .align-self-start </v-sheet>
        </v-col>

        <v-col align-self="center">
          <v-sheet class="pa-2 ma-2"> .align-self-center </v-sheet>
        </v-col>

        <v-col align-self="end">
          <v-sheet class="pa-2 ma-2"> .align-self-end </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
