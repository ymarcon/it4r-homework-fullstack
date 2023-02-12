<script setup lang="ts">
import { useCantonsStore } from "@/stores/cantons";
import { useChartOptions } from "@/utils/chart";
import type { EChartsOption } from "echarts";
import { PieChart } from "echarts/charts";
import { LegendComponent, TooltipComponent } from "echarts/components";
import { use } from "echarts/core";
import { SVGRenderer } from "echarts/renderers";
import VChart from "vue-echarts";
import { computed, ref } from "vue";
import type { Header, ClickRowArgument } from "vue3-easy-data-table";

use([SVGRenderer, PieChart, LegendComponent, TooltipComponent]);

const cantonsStore = useCantonsStore();

const headers: Header[] = [
  { text: "Code", value: "code", sortable: true },
  { text: "Name", value: "title", sortable: true },
  { text: "Male", value: "male", sortable: true },
  { text: "Female", value: "female", sortable: true },
  { text: "Other", value: "other", sortable: true },
];

const items = computed(() => {
  return cantonsStore.cantons;
});

const showCanton = (item: ClickRowArgument) => {
  selectedCanton.value = item.code;
};

const searchValue = ref();

const selectedCanton = ref<string>();

const selectedCantonTitle = computed<string>(() => {
  if (selectedCanton.value) {
    const canton = cantonsStore.cantons
      .filter((val) => val.code === selectedCanton.value)
      .pop();
    return canton ? canton.title : null;
  }
  return null;
});

const getCantonByCode = cantonsStore.getCantonByCode;
const chartOption = computed<EChartsOption>(() => {
  const count = getCantonByCode(selectedCanton.value);
  return useChartOptions(count);
});
</script>

<template>
  <div>
    <v-row>
      <v-col>
        <div class="text-h4 mb-3">Table Selection</div>
        <p class="font-weight-light mb-3">
          Select a canton to see its gender statistics.
        </p>
        <v-text-field label="Search" v-model="searchValue"></v-text-field>
        <EasyDataTable :headers="headers" :items="items" :rowsPerPage="10" @click-row="showCanton" search-field="title"
          :search-value="searchValue" />
      </v-col>
    </v-row>
    <v-row v-if="selectedCantonTitle">
      <v-col>
        <div class="text-h4" style="text-align: center;">{{ selectedCantonTitle }}</div>
        <v-responsive aspect-ratio="2">
          <v-chart :option="chartOption" />
        </v-responsive>
      </v-col>
    </v-row>
  </div>
</template>
