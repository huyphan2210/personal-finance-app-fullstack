// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2024-11-01",
  css: ["./assets/styles/default.scss"],
  devtools: { enabled: true },
  pages: true,
  modules: ["@pinia/nuxt", "@clerk/nuxt"],
  ssr: false,
  components: true,
});
