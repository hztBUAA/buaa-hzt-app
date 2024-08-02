<template>
  <v-container>
    <v-layout>
      <v-navigation-drawer expand-on-hover permanent rail>
        <v-list>
          <v-list-item
            prepend-avatar="https://randomuser.me/api/portraits/women/85.jpg"
            subtitle="sandra_a88@gmailcom"
            title="Sandra Adams"
          ></v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list density="compact" nav>
          <v-list-item
            prepend-icon="mdi-folder"
            title="My Files"
            value="myfiles"
          ></v-list-item>
          <v-list-item
            prepend-icon="mdi-account-multiple"
            title="Shared with me"
            value="shared"
          ></v-list-item>
          <v-list-item
            prepend-icon="mdi-star"
            title="Starred"
            value="starred"
          ></v-list-item>
        </v-list>
      </v-navigation-drawer>

      <v-main style="height: 400px"></v-main>
    </v-layout>
    <v-divider></v-divider>
    <v-card
      class="mb-1"
      :loading="isLoading"
      title="Card title"
      subtitle="Subtitle"
      text="..."
      variant="tonal"
      v-for="n in 3"
      :key="n"
    ></v-card>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      isLoading: false // Initialize loading state
    };
  },
  methods: {
    loadData() {
      this.isLoading = true; // Start loading
      // Simulate an async operation
      setTimeout(() => {
        // Your loading logic here
        this.isLoading = false; // End loading
      }, 2000); // Adjust the timeout as needed
    }
  },
  mounted() {
    this.loadData(); // Call the loading method when the component is mounted
  }
};
</script>
