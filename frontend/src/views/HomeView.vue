<script setup lang="ts">
const apiUrl = import.meta.env.VITE_API_URL;
</script>

<template>
  <v-container>
    <div class="text-h3">ENAC-IT4R Homework Full Stack</div>
    <p class="mt-3">
      Different ways of selecting the Canton of interest are proposed.
    </p>
    <p class="mt-3">The first one is a classic dropdown selection.</p>
    <v-btn variant="outlined" color="primary" class="mt-3" to="/select">
      Try Dropdown Selection
    </v-btn>
    <p class="mt-3">The second one consists of selecting the canton feature on the Swiss map. The data is a GeoJSON
      document, including both the geometry and the statistical properties of interest of each canton.</p>
    <v-btn variant="outlined" color="primary" class="mt-3" to="/map">
      Try Map Selection
    </v-btn>

    <p class="mt-3">The third one is using a table, which is convenient for filtering and sorting.</p>
    <v-btn variant="outlined" color="primary" class="mt-3" to="/table">
      Try Table Selection
    </v-btn>

    <p class="mt-3">The data can also be downloaded as a CSV file.</p>
    <v-btn variant="outlined" color="primary" class="mt-3" :href="apiUrl + '/cantons-csv'">
      Download CSV
    </v-btn>

    <p class="mt-3">The data are accessible through a public API.</p>
    <v-btn variant="outlined" color="primary" class="mt-3" :href="apiUrl + '/docs'" target="_blank">
      See API Docs
    </v-btn>
  </v-container>
</template>
