<script setup lang="ts">
import { RouterView } from "vue-router";
</script>

<template>
  <v-app>
    <v-app-bar color="primary" density="compact">
      <v-tabs>
        <v-tab to="/" prepend-icon="$home">
          <v-app-bar-title>Homework</v-app-bar-title>
        </v-tab>
      </v-tabs>
    </v-app-bar>
    <v-main>
      <RouterView />
    </v-main>
  </v-app>
</template>
