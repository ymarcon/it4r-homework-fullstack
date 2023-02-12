import type { Canton } from "@/models/canton.model";

export function useChartOptions(item: Canton) {
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
          { value: item.female, name: "Female" },
          { value: item.male, name: "Male" },
          { value: item.other, name: "Other" },
        ],
      },
    ],
  };
}