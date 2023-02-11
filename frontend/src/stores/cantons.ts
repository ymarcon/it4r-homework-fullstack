import axios from "axios";
import { defineStore } from "pinia";

export const useCantonsStore = defineStore("cantons", {
  state: () => ({
    cantons: {},
  }),
  getters: {
    getCantons(state) {
      return state.cantons;
    },
  },
  actions: {
    async fetchCantons() {
      try {
        const data = await axios.get("http://127.0.0.1:8000/cantons");
        this.cantons = data.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
  },
});
