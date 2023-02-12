<script setup lang="ts">
import { useCantonsStore } from "@/stores/cantons";
import { useCodesStore } from "@/stores/codes";
import type { EChartsOption } from "echarts";
import { PieChart } from "echarts/charts";
import { LegendComponent, TooltipComponent } from "echarts/components";
import { use } from "echarts/core";
import { SVGRenderer } from "echarts/renderers";
import { computed, onMounted, ref } from "vue";
import VChart from "vue-echarts";

use([SVGRenderer, PieChart, LegendComponent, TooltipComponent]);

const cantonsStore = useCantonsStore();
const codesStore = useCodesStore();

onMounted(() => {
  cantonsStore.fetchCantons();
  codesStore.fetchCodes();
});

const codesItems = computed(() => {
  const items: { value: string; title: string }[] = [];
  const codes = codesStore.codes;
  Object.keys(codes)
    .sort()
    .forEach((key) => {
      items.push({
        value: key,
        title: codes[key],
      });
    });
  return items;
});

const selectedCanton = ref<string>();

const chartOption = computed<EChartsOption>(() => {
  const count = getGenderCount(selectedCanton.value);
  return {
    tooltip: {
      trigger: "item",
    },
    legend: {
      left: "center",
    },
    series: [
      {
        type: "pie",
        radius: ["40%", "80%"],
        data: [
          { value: count.female, name: "Female" },
          { value: count.male, name: "Male" },
          { value: count.other, name: "Other" },
        ],
      },
    ],
  };
});

function getGenderCount(canton?: string): {
  female?: number;
  male?: number;
  other?: number;
} {
  if (canton === undefined) {
    return {};
  }
  const counts = cantonsStore.cantons
    .filter((val) => val.code === canton)
    .pop();
  return counts
    ? {
      female: counts["female"] || 0,
      male: counts["male"] || 0,
      other: counts["other"] || 0,
    }
    : {
      female: 0,
      male: 0,
      other: 0,
    };
}
</script>

<template>
  <div>
    <v-row>
      <v-col>
        <v-select v-model="selectedCanton" label="Canton" :items="codesItems" />
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-responsive aspect-ratio="2">
          <v-chart :option="chartOption" />
        </v-responsive>
      </v-col>
    </v-row>
  </div>
</template>
