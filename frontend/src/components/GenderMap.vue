<script setup lang="ts">
import { useChartOptions } from "@/utils/chart";
import type { EChartsOption } from "echarts";
import { PieChart } from "echarts/charts";
import { LegendComponent, TooltipComponent } from "echarts/components";
import { use } from "echarts/core";
import { SVGRenderer } from "echarts/renderers";
import VChart from "vue-echarts";
import { computed, ref } from "vue";
import { GeoJSON } from "ol/format";
import { click } from "ol/events/condition";

use([SVGRenderer, PieChart, LegendComponent, TooltipComponent]);

const center = ref([8, 46.5]);
const projection = ref('EPSG:4326');
const zoom = ref(7.5);
const rotation = ref(0);
const url = ref(import.meta.env.VITE_API_URL + "/cantons-geo");
const geoJson = new GeoJSON();
const selectCondition = click;
const featureSelected = (event: any) => {
  if (event.selected.length == 1) {
    const feature = event.selected[0];
    selectedItem.value = feature.values_;
  } else {
    selectedItem.value = undefined;
  }
};

const selectedItem = ref();

const chartOption = computed<EChartsOption>(() => {
  const count = selectedItem.value;
  return useChartOptions(count);
});
</script>

<template>
  <div>
    <v-row>
      <v-col>
        <div class="text-h4 mb-3">Map Selection</div>
        <p class="font-weight-light mb-3">
          Select a canton to see its gender statistics.
        </p>
        <ol-map :loadTilesWhileAnimating="true" :loadTilesWhileInteracting="true" style="height:400px">
          <ol-view ref="view" :center="center" :rotation="rotation" :zoom="zoom" :projection="projection" />
          <ol-zoom-control />
          <ol-zoomslider-control />
          <ol-tile-layer>
            <ol-source-osm />
          </ol-tile-layer>
          <ol-vector-layer>
            <ol-source-vector :url="url" :format="geoJson"></ol-source-vector>
          </ol-vector-layer>

          <ol-interaction-select @select="featureSelected" :condition="selectCondition">
            <ol-style>
              <ol-style-stroke color="green" :width="3"></ol-style-stroke>
              <ol-style-fill color="rgba(255,255,255,0.5)"></ol-style-fill>
            </ol-style>
          </ol-interaction-select>
        </ol-map>
      </v-col>
    </v-row>
    <v-row v-if="selectedItem && selectedItem.title">
      <v-col>
        <div class="text-h4" style="text-align: center;">{{ selectedItem.title }}</div>
        <v-responsive aspect-ratio="2">
          <v-chart :option="chartOption" />
        </v-responsive>
      </v-col>
    </v-row>
  </div>
</template>
