<template>
  <v-container fluid>
    <v-row dense>
      <v-col v-for="c in cards" :key="c.id" cols="6">
        <v-card :subtitle="c.subtitle" :title="c.title" :text="c.content">
          <v-card-actions>
            <v-spacer></v-spacer>
            <!-- <v-btn density icon @click="like" stacked>
              <v-icon color="red">mdi-heart</v-icon>{{ 1 }}
            </v-btn>
            <v-btn density icon @click="bookmark" stacked>
              <v-icon>mdi-bookmark</v-icon>{{ 2 }}
            </v-btn>
            <v-btn density icon @click="share" stacked>
              <v-icon>mdi-share-variant</v-icon>
            </v-btn>
            <v-btn density icon @click="refresh">
              <v-icon>mdi-refresh</v-icon>
            </v-btn> -->
            <v-list-item class="w-100">
              <template v-slot:prepend>
                <v-avatar color="grey-darken-3" :image="c.avatar"></v-avatar>
              </template>

              <v-list-item-title>{{ c.title }}</v-list-item-title>

              <v-list-item-subtitle>{{ c.subtitle }}</v-list-item-subtitle>

              <template v-slot:append>
                <div justify="left">
                  <v-icon
                    class="me-1"
                    :color="c.liked ? 'red' : ''"
                    icon="mdi-heart"
                    @click="like(c.id)"
                  ></v-icon>
                  <span class="subheading me-2" aria-label="like">{{
                    c.likes
                  }}</span>
                  <span class="me-1">·</span>
                  <v-icon
                    class="me-1"
                    icon="mdi-share-variant"
                    @click="share"
                  ></v-icon>
                  <span class="subheading">45</span>
                </div>
              </template>
            </v-list-item>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <router-view></router-view>
    </v-row>

  </v-container>
</template>

<script>
import axios from '@/plugins/axios';
export default {
  data: () => ({
    cards: []
  }),
  mounted() {
    this.cards = this.fetchBlogs();
  },
  methods: {
    
    async fetchBlogs() {
      try {
        const response = await axios.get('posts/');
        this.cards = response.data.map((card) => ({
          ...card,
          avatar: this.getRandomAvatar(), // Fetch random avatar
          liked: card.liked || false // Assume the backend returns the liked status
        }));
      } catch (error) {
        console.error('Error fetching blogs:', error);
      }
    },
    getRandomAvatar() {
      // Generate a random seed for the avatar
      const seed = Math.random().toString(36).substring(7);
      return `https://api.dicebear.com/9.x/pixel-art/svg?seed=${seed}`;
    },
    async like(cardId) {
      const card = this.cards.find((c) => c.id === cardId);
      if (card) {
        card.liked = !card.liked;
        card.likes += card.liked ? 1 : -1;
        try {
          await axios.post(`posts/${cardId}/likes`, { liked: card.liked });
        } catch (error) {
          console.error('Error updating like status:', error);
        }
      }
    },
    bookmark() {
      console.log('bookmark');
    },
    share() {
      console.log('share');
    },
    refresh() {
      console.log('refresh');
    }
  }
};
</script>
