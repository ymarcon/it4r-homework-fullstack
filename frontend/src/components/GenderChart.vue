<script setup lang="ts">
import { cantons } from "@/utils/canton";
import type { EChartsOption } from "echarts";
import { PieChart } from "echarts/charts";
import { LegendComponent, TooltipComponent } from "echarts/components";
import { use } from "echarts/core";
import { SVGRenderer } from "echarts/renderers";
import { random } from "lodash";
import { computed, ref } from "vue";
import VChart from "vue-echarts";

use([SVGRenderer, PieChart, LegendComponent, TooltipComponent]);

const cantonItems: { title: string; value: string }[] = cantons.map(
  (canton) => ({
    title: canton.name,
    value: canton.id,
  })
);

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
  return {
    female: random(1024),
    male: random(1024),
    other: random(1024),
  };
}
</script>

<template>
  <v-row>
    <v-col>
      <v-select v-model="selectedCanton" label="Canton" :items="cantonItems" />
    </v-col>
  </v-row>
  <v-row>
    <v-col>
      <v-responsive aspect-ratio="2">
        <v-chart :option="chartOption" />
      </v-responsive>
    </v-col>
  </v-row>
</template>
