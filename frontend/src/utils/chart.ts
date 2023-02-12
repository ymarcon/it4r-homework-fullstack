import type { Canton } from "@/models/canton.model";
import type { EChartsOption } from "echarts";

export function useChartOptions(item: Canton | undefined): EChartsOption {
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
          { value: item ? item.female : 0, name: "Female" },
          { value: item ? item.male : 0, name: "Male" },
          { value: item ? item.other : 0, name: "Other" },
        ],
      },
    ],
  };
}