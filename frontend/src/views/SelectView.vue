<script setup lang="ts">
import { useCantonsStore } from "@/stores/cantons";
import { useCodesStore } from "@/stores/codes";
import { onMounted } from "vue";
import GenderSelect from "../components/GenderSelect.vue";

const cantonsStore = useCantonsStore();
const codesStore = useCodesStore();

onMounted(() => {
  cantonsStore.fetchCantons();
  codesStore.fetchCodes();
});
</script>

<template>
  <v-container>
    <GenderSelect />
  </v-container>
</template>
