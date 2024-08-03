<template>
  <v-chip-group v-bind="chipGroupProps">
    <v-chip>Chip 1</v-chip>
    <v-chip>Chip 2</v-chip>
    <v-chip>Chip 3</v-chip>
    <!-- More chips -->
  </v-chip-group>
  <v-btn @click="changeVisibility" color="blue">Change visibility</v-btn>
  <v-btn @click="changeVisibility" :color="red">Change visibility</v-btn>
  <v-btn @click="changeDraggability">Change draggability</v-btn>
</template>

<script>
export default {
  data() {
    return {
      chipGroupProps: {
        draggable: true,
        disabled: false
      },
      red: 'red'
    };
  },
  methods: {
    changeVisibility() {
      this.chipGroupProps.disabled = !this.chipGroupProps.disabled;
      switch (this.red) {
        case 'red':
          this.red = 'purple';
          break;
        case 'purple':
          this.red = 'success';
          break;
        case 'success':
          this.red = 'error';
          break;
        default:
          this.red = 'green';
          break;
      }
      // this.red = (red == 'red' ? 'blue' : re'red');
    },
    changeDraggability() {
      this.chipGroupProps.draggable = !this.chipGroupProps.draggable;
    }
  }
};
</script>
