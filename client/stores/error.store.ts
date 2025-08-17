interface ErrorState {
  message: string;
  isError: boolean;
}

export const DEFAULT_ERROR_MESSAGE =
  "Something's wrong! Please contact the developer.";

export const useErrorStore = defineStore("error", {
  state: (): ErrorState => ({
    message: "",
    isError: false,
  }),
  actions: {
    setErrorMessage(message: string) {
      this.message = message;
      if (!this.message) {
        this.isError = false;
      } else {
        this.isError = true;
      }
    },
    setDefaultErrorMessage() {
      this.message = DEFAULT_ERROR_MESSAGE;
      this.isError = true;
    },
  },
});
