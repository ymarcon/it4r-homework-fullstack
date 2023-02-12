import axios from "axios";
import { defineStore } from "pinia";
import type { Cantons } from "@/models/canton.model";

export type CantonsState = {
  cantons: Cantons;
};

export const useCantonsStore = defineStore("cantons", {
  state: () => ({
    cantons: [],
  } as CantonsState),
  getters: {
    getCantons(state) {
      return state.cantons;
    },
  },
  actions: {
    async fetchCantons() {
      try {
        const data = await axios.get(import.meta.env.VITE_API_URL + "/cantons");
        this.cantons = data.data;
      } catch (error: any) {
        alert(error.response.data.detail);
        console.log(error);
      }
    },
  },
});
