<script setup lang="ts">
import { useCantonsStore } from "@/stores/cantons";
import { useCodesStore } from "@/stores/codes";
import type { EChartsOption } from "echarts";
import { PieChart } from "echarts/charts";
import { LegendComponent, TooltipComponent } from "echarts/components";
import { use } from "echarts/core";
import { SVGRenderer } from "echarts/renderers";
import VChart from "vue-echarts";
import { computed, ref } from "vue";

use([SVGRenderer, PieChart, LegendComponent, TooltipComponent]);

const cantonsStore = useCantonsStore();
const codesStore = useCodesStore();

const codesItems = computed(() => {
  const items: { value: string; title: string }[] = codesStore.codes
    .map((code) => {
      return {
        value: code.code,
        title: code.canton,
      };
    })
    .sort((a, b) => {
      if (a.title < b.title) {
        return -1;
      }
      if (a.title > b.title) {
        return 1;
      }
      return 0;
    });
  return items;
});

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
        <div class="text-h4 mb-3">
          Dropdown Selection
        </div>
        <p class="font-weight-light mb-3">
          Select a canton to see its gender statistics.
        </p>
        <v-select v-model="selectedCanton" label="Canton" :items="codesItems" />
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
