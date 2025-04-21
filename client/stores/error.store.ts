interface ErrorState {
  message: string;
  isError: boolean;
}

export const useErrorStore = defineStore("error", {
  state: (): ErrorState => ({
    message: "",
    isError: false
  }),
  actions: {
    setErrorMessage(message: string) {
      this.message = message;
      if (!this.message) {
        this.isError = false;
      } else {
        this.isError = true;
      }
    }
  },
});