<template>
  <div class="text-center ma-2">
    <v-btn @click="snackbar = true" :variant='btnVariant'> Open Snackbar </v-btn>
    <v-btn @click.stop="changeBtnVariant">Change Variant</v-btn>
    <v-snackbar v-model="snackbar">
      {{ text }}

      <template v-slot:actions>
        <v-btn color="pink" variant="text" @click="snackbar = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>
<script>
export default {
  data: () => ({
    snackbar: false,
    text: `Hello, I'm a snackbar`,
    btnVariant: 'outlined'
  })
  ,methods: {
    changeBtnVariant() {
      console.log('changeBtnVariant')
      const variants = ['text', 'outlined', 'flat', 'plain', 'tonal','elevated']
      this.btnVariant = variants[Math.floor(Math.random() * variants.length)]
    }
  }
};
</script>
