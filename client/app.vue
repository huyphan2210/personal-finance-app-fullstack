<template>
  <NuxtRouteAnnouncer />
  <NuxtPage />
</template>

<style lang="scss">
* {
  margin: 0;
  padding: 0;
  overflow: hidden;
}

:root {
  --beige-100: #f8f4f0;
  --beige-500: #98908b;

  --grey-100: #f2f2f2;
  --grey-300: #b3b3b3;
  --grey-500: #696868;
  --grey-900: #201f24;
}

body {
  background-color: var(--beige-100);
  min-height: 100vh;
}
</style>
