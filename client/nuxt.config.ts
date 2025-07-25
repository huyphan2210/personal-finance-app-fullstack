// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2024-11-01",
  css: ["./assets/styles/default.scss"],
  devtools: { enabled: true },
  pages: true,
  modules: ["@pinia/nuxt", "@clerk/nuxt"],
  ssr: false,
  components: true,
  vite: {
    css: {
      preprocessorOptions: {
        scss: {
          additionalData: `
            @use "@/assets/styles/fonts" as *;
            @use "@/assets/styles/form" as *;
            @use "@/assets/styles/animations" as *;
            @use "@/assets/styles/utilities" as *;
          `,
        },
      },
    },
  },
  runtimeConfig: {
    public: {
      apiBase: "http://127.0.0.1:5000/api",
    },
  },
});
