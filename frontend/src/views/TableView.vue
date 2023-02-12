<script setup lang="ts">
import { useCantonsStore } from "@/stores/cantons";
import { onMounted } from "vue";
import GenderTable from "../components/GenderTable.vue";

const cantonsStore = useCantonsStore();

onMounted(() => {
  cantonsStore.fetchCantons();
});
</script>

<template>
  <v-container>
    <GenderTable />
  </v-container>
</template>
