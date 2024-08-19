<template>
  <v-container>
    <v-sparkline
      :auto-line-width="autoLineWidth"
      :fill="fill"
      :gradient="gradient"
      :gradient-direction="gradientDirection"
      :line-width="width"
      :model-value="value"
      :padding="padding"
      :smooth="radius || false"
      :stroke-linecap="lineCap"
      :type="type"
      auto-draw
    ></v-sparkline>
    <v-speed-dial location="right center" transition="fade-transition">
      <template v-slot:activator="{ props: activatorProps }">
        <v-fab v-bind="activatorProps" size="large" icon="$vuetify"></v-fab>
      </template>

      <v-btn key="1" icon="$success"></v-btn>
      <v-btn key="2" icon="$info"></v-btn>
      <v-btn key="3" icon="$warning"></v-btn>
      <v-btn key="4" icon="$error"></v-btn>
    </v-speed-dial>
  </v-container>
</template>
<script>
const gradients = [
  ['#222'],
  ['#42b3f4'],
  ['red', 'orange', 'yellow'],
  ['purple', 'violet'],
  ['#00c6ff', '#F0F', '#FF0'],
  ['#f72047', '#ffd200', '#1feaea']
];

export default {
  data: () => ({
    width: 2,
    radius: 10,
    padding: 8,
    lineCap: 'round',
    gradient: gradients[5],
    value: [0, 2, 5, 9, 5, 10, 3, 5, 0, 0, 1, 8, 2, 9, 0],
    gradientDirection: 'top',
    gradients,
    fill: false,
    type: 'trend',
    autoLineWidth: false
  })
};
</script>
