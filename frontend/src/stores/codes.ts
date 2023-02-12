import axios from "axios";
import { defineStore } from "pinia";
import type { Codes } from "@/models/code.model";

export type CodesState = {
  codes: Codes;
};

export const useCodesStore = defineStore("codes", {
  state: () => ({
    codes: [],
  } as CodesState),
  getters: {
    getCodes(state) {
      return state.codes;
    },
  },
  actions: {
    async fetchCodes() {
      try {
        const data = await axios.get(import.meta.env.VITE_API_URL + "/codes");
        this.codes = data.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
  },
});
